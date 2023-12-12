from ag.ag import AG
from individuos.individuo import CriarIndividuo, Individuo
from mapa.mapa import Mapa

import matplotlib.pyplot as plt
from copy import copy

import json
import os

#grafico
fitness_melhor_individuo = []
media_fitness_populacao = []
quantidade_de_grama = []

#grafico
contador = 0 #contador para plotar graficos
numero_do_grafico = 0 #contador dos graficos
contador_quantidade = 2000 #quantidade que o contador deve chegar para plotar um grafico


#mutação variada
contador_mutacao_variada = 0 #contador da mutacao_variada
contador_mutacao_variada_quantidade = 1000 #quantidade que o contador deve chegar para fazer uma mutação variada
index_mutacao_variada = 0 #index para ver a quantidade de mutações a ser feita
mutacoes_variadas = [1, 5, 10, 20, 10, 5, 1, -1] #vetor da quantidade de mutações a ser feita
delta_fitness = 0
DIFERENCA = 0 #diferença para que ele faça uma mutação variada

melhor_de_todos: Individuo 


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

        global delta_fitness
        global mutacoes_variadas
        global index_mutacao_variada

        populacao = Ordernar(populacao) #ordernar a população (melhores no inicio)

        nova_populacao: list[Individuo] = []

        fitness_anterior = melhor_de_todos.quantidade

        #tenho o melhor de todos

        for individuo in populacao:
            individuo.quantidade = individuo.quantidade / 100

        for i in range(len(populacao)):
            if populacao[i].quantidade > melhor_de_todos.quantidade:
                melhor_de_todos = copy(populacao[i])

        fitness_posterior = melhor_de_todos.quantidade

        delta_fitness = fitness_posterior - fitness_anterior
        
        gene_melhor_de_todos = copy(melhor_de_todos.gene)

        posicao = self.mapa.posicao_disponivel(tipo) #pegar uma nova posição
        nova_populacao.append(CriarIndividuo(gene=gene_melhor_de_todos, posicao=posicao, tipo=tipo)) #adicionar o melhor de todos na população

        posicao = self.mapa.posicao_disponivel(tipo) #pegar uma nova posição
        nova_populacao.append(CriarIndividuo(gene=ag.mutate(gene_melhor_de_todos, mutacoes_variadas[index_mutacao_variada]), posicao=posicao, tipo=tipo)) #adicionar o melhor de todos mutado

        media_dos_fitness: int = 0 #media do fitness da população

        #a melhor metade da população
        for i in range(int(len(populacao)/2)):
            posicao = self.mapa.posicao_disponivel(tipo) #pegar uma nova posição
            nova_populacao.append(CriarIndividuo(gene=ag.mutate(populacao[i].gene, mutacoes_variadas[index_mutacao_variada]), posicao=posicao, tipo=tipo)) #passar o cara mutado
            media_dos_fitness += populacao[i].quantidade

        #pior metade da população
        for i in range(int(len(populacao)/2), len(populacao) - 2):
            media_dos_fitness += populacao[i].quantidade #calcula a media 

            populacao[i] = copy(melhor_de_todos)
            gene = populacao[i].gene
            #gene = cruzamento(melhor_de_todos, pai2) #cruzar com o melhor de todos
            gene = ag.mutate(gene, mutacoes_variadas[index_mutacao_variada]) #mutar o gene

            posicao = self.mapa.posicao_disponivel(tipo) #pegar uma nova posição
            nova_populacao.append(CriarIndividuo(gene=gene, posicao=posicao, tipo=tipo)) #adicionar o novo cara na população
        
        media_dos_fitness /= len(populacao) #calcula media
        print("MEDIA DOS FITNESS: ", media_dos_fitness)
        print("TAMANHO POP: ", len(populacao))
        media_fitness_populacao.append(media_dos_fitness) #adiciona media

        fitness_melhor_individuo.append(melhor_de_todos.quantidade)
        print("FITNESS DO MELHOR: ", fitness_melhor_individuo)

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

    def Genocidio(self):
        global melhor_de_todos

        self.mapa = Mapa(50, 50, obstaculo_chance=0, terra_chance=0.50, grama_chance=0.80) #criar um novo mapa

        #criar uma nova população totalmente nova
        nova_populacao: list[Individuo] = self.StartPopulation(numero_de_individuos=self.numero_de_indivudos - 1, gene=[[[[0, 0], [4, None], [5, None], [6, None], [7, None]], [[1, 0], [4, None], [5, None], [6, None], [7, None]], [[2, 0], [4, None], [5, None], [6, None], [7, None]], [[3, 0], [4, None], [5, None], [6, None], [7, None]]], [[[4, None]], [[5, None]], [[6, None]], [[7, None]], [[8, None]]]])

        posicao = self.mapa.posicao_disponivel(melhor_de_todos.tipo) #pegar uma nova posicao
        nova_populacao.append(CriarIndividuo(gene=melhor_de_todos.gene, posicao=posicao, tipo=melhor_de_todos.tipo)) #colocar o melhor de todos na população

        return nova_populacao
            

    def StartSimulation(self, numero_de_geracoes: int, numero_de_individuos: int, numero_de_acoes: int, gene_individuo: list):
        global melhor_de_todos

        #plotar gráfico
        global contador
        global contador_quantidade

        #mutação variada
        global contador_mutacao_variada
        global contador_mutacao_variada_quantidade
        global index_mutacao_variada
        global mutacoes_variadas
        global delta_fitness

        self.numero_de_geracoes = numero_de_geracoes
        self.numero_de_indivudos = numero_de_individuos
        self.numero_de_acoes = numero_de_acoes

        self.mapa = Mapa(50, 50, obstaculo_chance=0, terra_chance=0.50, grama_chance=0.50)

        self.individuos = self.StartPopulation(numero_de_individuos=numero_de_individuos, gene=gene_individuo)

        melhor_de_todos = self.individuos[0]

        geracao = 0

        while(True):
            print("Na geração: ", geracao)

            if delta_fitness == DIFERENCA:
                contador_mutacao_variada += 1

                if (contador_mutacao_variada >= contador_mutacao_variada_quantidade):
                    print("Mudou mutação")
                    index_mutacao_variada = (index_mutacao_variada + 1) % len(mutacoes_variadas) #atualizar o index (circular)

                    contador_mutacao_variada = 0

                    if mutacoes_variadas[index_mutacao_variada] == -1: #fazer um genocidio
                        self.individuos = self.Genocidio()

                        print("Genocídio")
                        
                        index_mutacao_variada = 0 #zerar a mutação variada
            else: 
                contador_mutacao_variada = 0
            
            if contador == contador_quantidade:
                contador = 0

                self.Plotar_Grafico()



            self.Simulate()
   
            for i in self.individuos:
                i.resetar_vida_fome()
            self.mapa = Mapa(50, 50, obstaculo_chance=0, terra_chance=0.50, grama_chance=0.80)

            if geracao % 100 == 0 and geracao > 0:
                for idv in self.individuos:
                 print(f"quantos comeu {idv.quantidade}")

                print("CRIOU NOVA POPULACAO!")
                self.individuos = self.nova_populacao(self.individuos, self.individuos[0].tipo)

            contador += 1

            geracao += 1

                
    def Plotar_Grafico(self):
        global melhor_de_todos
        global numero_do_grafico

        # Gerações (assumindo que cada elemento nas listas acima corresponde a uma geração)
        geracoes = list(range(1, (len(fitness_melhor_individuo) + 1))) 

        # Criar o gráfico
        plt.plot(geracoes, fitness_melhor_individuo, label='Melhor Indivíduo')
        plt.plot(geracoes, media_fitness_populacao, label='Média da População')
        #plt.plot(geracoes, quantidade_de_grama, label='Quantidade de grama')

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