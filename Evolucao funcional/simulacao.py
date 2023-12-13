from ag.ag import AG
from individuos.individuo import CriarIndividuo, Individuo
from mapa.mapa import Mapa

import matplotlib.pyplot as plt
from copy import copy

import json
import os

fitness_melhor_individuo = []
media_fitness_populacao = []
quantidade_de_grama = []

fintess_melhor_geracao = []

contador = 0
numero_do_grafico = 0

contador_quantidade = 1000

melhor_de_todos: Individuo 

mutacao_variavel = [0, 1, 1, 1, 0]
index_mutacao = 0
DELTA = 0.5
delta_fitness = 0

contador_variavel = 0
contador_variavel_qtd = 500

ag = AG()

def Ordernar(individuos):
    def criterio_de_ordenacao(individuo):
        return individuo.quantidade

    return sorted(individuos, key=criterio_de_ordenacao, reverse=True)

def melhor_individuo(individuo1: Individuo, individuo2: Individuo):
    if individuo1.quantidade > individuo2.quantidade:
        return individuo1
    return individuo2

def cruzamento(individuo1: Individuo, individuo2: Individuo):
    gene_novo = individuo1.gene.copy()

    for i in range(len(individuo1.gene)):
        for j in range(len(individuo1.gene[i])):

            neuronio1_info: list = individuo1.gene[i][j]
            neuronio2_info: list = individuo2.gene[i][j]

            for k in range(0, len(neuronio1_info)):
                gene_novo[i][j][k][1] = (neuronio1_info[k][1] + neuronio2_info[k][1]) / 2

    return gene_novo


class Simulacao():
    def __init__(self) -> None:
        pass

    def nova_populacao(self, populacao: list[Individuo], tipo: int)->list:
        global melhor_de_todos
        global fintess_melhor_geracao

        global mutacao_variavel
        global index_mutacao

        global delta_fitness

        populacao = Ordernar(populacao) #ordernar a população (melhores no inicio)

        nova_populacao: list[Individuo] = []

        melhor_da_populacao = populacao[0]

        anterior_fintess = melhor_da_populacao.quantidade

        #tenho o melhor de todos
        for i in range(len(populacao)):
            if populacao[i].quantidade >= melhor_de_todos.quantidade:
                melhor_de_todos = copy(populacao[i])

            if populacao[i].quantidade > melhor_da_populacao.quantidade:
                melhor_da_populacao = copy(populacao[i])

        posterior_fitness = melhor_da_populacao.quantidade

        delta_fitness = abs(posterior_fitness - anterior_fintess)
    
        fintess_melhor_geracao.append(melhor_da_populacao.quantidade)

        gene_melhor_de_todos = copy(melhor_de_todos.gene)

        posicao = self.mapa.posicao_disponivel(3) #pegar uma nova posição
        nova_populacao.append(CriarIndividuo(gene=gene_melhor_de_todos, posicao=posicao, tipo=tipo)) #adicionar o melhor de todos na população

        posicao = self.mapa.posicao_disponivel(3) #pegar uma nova posição
        nova_populacao.append(CriarIndividuo(gene=melhor_da_populacao.gene, posicao=posicao, tipo=tipo)) #adicionar o melhor de todos mutado

        media_dos_fitness: int = 0 #media do fitness da população

        
        #a melhor metade da população
        for i in range(int(len(populacao)/2)):
            media_dos_fitness += populacao[i].quantidade #calcula a media

            pai = populacao[i]

            gene = cruzamento(melhor_da_populacao, pai)

            posicao = self.mapa.posicao_disponivel(tipo) #pegar uma nova posição
            nova_populacao.append(CriarIndividuo(gene=gene, posicao=posicao, tipo=tipo)) #passar o cara mutado
        

        #pior metade da população
        for i in range(int(len(populacao)/2), len(populacao) - 2):
            media_dos_fitness += populacao[i].quantidade #calcula a media 

            pai2 = populacao[i]

            gene = cruzamento(melhor_de_todos, pai2) #cruzar com o melhor de todos
            #gene = ag.mutate(melhor_da_populacao.gene, 1) #mutar o gene

            posicao = self.mapa.posicao_disponivel(tipo) #pegar uma nova posição
            nova_populacao.append(CriarIndividuo(gene=gene, posicao=posicao, tipo=tipo)) #adicionar o novo cara na população
        
        media_dos_fitness /= len(populacao) #calcula media
        media_fitness_populacao.append(media_dos_fitness) #adiciona media

        fitness_melhor_individuo.append(melhor_de_todos.quantidade)

        return nova_populacao
    
    def StartPopulation(self, numero_de_individuos: int, gene: list):
        individuos = []

        for _ in range(numero_de_individuos):
                posicao = self.mapa.posicao_disponivel(3)

                individuos.append(CriarIndividuo(gene=gene, posicao=posicao, tipo=3))

        return individuos

    def Simulate(self):
        for acao in range(self.numero_de_acoes):
            for i in range(len(self.individuos)):
                inputs = self.mapa.inputs(self.individuos[i].posicao) #pegar os inputs para esse individuo

                predicao = self.individuos[i].network.predict(inputs) #fazer a predicao

                #ver qual ação deve ser feita
                acao = predicao.index(max(predicao))

                #fazer a ação e pegar a nova posição do indivíduo após a ação

                nova_posicao, resultado = self.mapa.make_action(acao, self.individuos[i].posicao)
                self.individuos[i].posicao = nova_posicao 

                if resultado == -1:
                    self.individuos[i].quantidade += 1
                else:
                    self.individuos[i].quantidade -= 1

            

    def StartSimulation(self, numero_de_geracoes: int, numero_de_individuos: int, numero_de_acoes: int, gene_individuo: list):
        global melhor_de_todos
        global contador
        global contador_quantidade

        global contador_variavel
        global contador_variavel_qtd
        global index_mutacao
        global mutacao_variavel

        self.numero_de_geracoes = numero_de_geracoes
        self.numero_de_indivudos = numero_de_individuos
        self.numero_de_acoes = numero_de_acoes

        self.mapa = Mapa(50, 50, obstaculo_chance=0, terra_chance=0.5, grama_chance=0.5)

        self.individuos = self.StartPopulation(numero_de_individuos=numero_de_individuos, gene=gene_individuo)

        melhor_de_todos = self.individuos[0]

        geracao = 0

        while(True):
            print("Na geração: ", geracao)
            geracao +=1

            if delta_fitness <= DELTA:
                contador_variavel += 1

                if contador_variavel >= contador_variavel_qtd:
                    index_mutacao = (index_mutacao + 1) % len(mutacao_variavel)
            
            if contador == contador_quantidade:
                contador = 0

                self.Plotar_Grafico()

            self.Simulate()

            for individuo in self.individuos:
                posicao = individuo.posicao

                if posicao in self.mapa.positions_withgrass:
                    self.mapa.mudar_valor(posicao, 2)
                else: self.mapa.mudar_valor(posicao, 0)

            #self.mapa = Mapa(50, 50, obstaculo_chance=0, terra_chance=0.50, grama_chance=0.50)

            self.individuos = self.nova_populacao(self.individuos, self.individuos[0].tipo)

            contador += 1

            
            
    def Plotar_Grafico(self):
        global melhor_de_todos
        global numero_do_grafico
        global fintess_melhor_geracao

        # Gerações (assumindo que cada elemento nas listas acima corresponde a uma geração)
        geracoes = list(range(1, len(fitness_melhor_individuo) + 1))

        # Criar o gráfico
        plt.plot(geracoes, fitness_melhor_individuo, label='Melhor Indivíduo')
        plt.plot(geracoes, media_fitness_populacao, label='Média da População')
        plt.plot(geracoes, fintess_melhor_geracao, label='Melhor da geracao')

        # Adicionar legendas e títulos
        plt.xlabel('Geração')
        plt.ylabel('Fitness')
        plt.title('Evolução do Fitness ao Longo das Gerações')
        plt.legend()

        diretorio = os.path.join("graficos", str(numero_do_grafico) + ".png")

        # Mostrar o gráfico
        plt.savefig(diretorio)
        plt.close()

        with open(os.path.join("genes", str(numero_do_grafico) + ".json"), "w") as f:
            json.dump(melhor_de_todos.gene, f)

        numero_do_grafico += 1 #atualizar o numero do grafico