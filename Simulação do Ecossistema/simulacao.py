from individuos.individuo import CriarIndividuo, Individuo
from mapa.mapa import Mapa

import matplotlib.pyplot as plt
from copy import copy

import os

import random


melhor_de_todos_presa: Individuo
melhor_presa_fitness_geracao_anterior: int
grafico_melhor_presa: list = []
grafico_media_presa: list = []

melhor_de_todos_predador: Individuo
melhor_predador_fitness_geracao_anterior: int
grafico_melhor_predador: list = []
grafico_media_predador: list = []

#grafico
contador = 0
numero_do_grafico = 0
contador_quantidade = 500

#mutação variada
index_mutacao_presa = 0
mutacao_variada_presa = [0, 1, 2]
contador_variacao_presa = 0
quantidade_variacao_presa = 300
contador_bem_presa = 0
bem_quantidade_presa = 10

index_mutacao_predador = 0
mutacao_variada_predador = [0, 1, 2]
contador_variacao_predador = 0
quantidade_variacao_predadir = 300
contador_bem_predador = 0
bem_quantidade_predador = 10


def mutate(gene, qnt) -> list:
    for _ in range(qnt): #pela quantidade de vezes que se deve mutar
        locus = random.randint(0, len(gene) - 1) #escolhe randomicamente um locus

        gene[locus] = random.randint(0, 4) #escolhe uma ação aleatória para esse locus

    return gene

def Ordernar(individuos) -> list[Individuo]:
    """Ordena uma lista de indivíduos pela sua quantidade (fitness)"""
    def criterio_de_ordenacao(individuo):
        return individuo.quantidade

    return sorted(individuos, key=criterio_de_ordenacao, reverse=True)

def cruzamento(melhor_de_todos: Individuo, individuo: Individuo) -> list:
    gene_novo = copy(individuo.gene) #copia o gene de um dos indivíduos

    for i in range(len(gene_novo)): #para cada locus
        pegar_do_melhor = random.choices([0, 1], weights=[0.8, 0.2])[0] #tem uma chance de 80% de pegar o gene do melhor

        if pegar_do_melhor:
            gene_novo[i] = melhor_de_todos.gene[i]
        else:
            gene_novo[i] = individuo.gene[i]

    return gene_novo

class Simulacao():
    def __init__(self) -> None:
        pass

    def AdicionarIndividuo(self, gene, mapeamento, tipo) -> Individuo:
        """Retorna um novo indivíduo já inserido no mapa"""
        posicao = self.mapa.posicao_disponivel(tipo)
        return CriarIndividuo(gene=gene, mapeamento=mapeamento, posicao=posicao, tipo=tipo)

    def nova_populacao_presas(self, populacao: list[Individuo])-> list[Individuo]:
        #---------------------Globais---------------------
        global melhor_de_todos_presa
        global melhor_presa_fitness_geracao_anterior
        global grafico_melhor_presa
        global grafico_media_presa

        global index_mutacao_presa
        global contador_bem_presa

        #---------------------Ordenacao---------------------
        nova_populacao = [] #lista com os indivíduos da nova população
        media_populacao = 0 #variável para o cáculo da média da população

        populacao = Ordernar(populacao) #ordernar a população atual
        
        #---------------------Mutação Variada---------------------
        #se o melhor de todos teve um desempenho muito ruim
        if (abs(populacao[0].quantidade)) <= (abs(melhor_presa_fitness_geracao_anterior) / 2):
            #aumentar o index da taxa de mutação
            index_mutacao_presa = (index_mutacao_presa + 1) % len(mutacao_variada_presa) 

            if index_mutacao_presa == 0: #ter certeza que a necessidade de uma mutação variada nao leve a 0 de mutação
                index_mutacao_presa = 1

            contador_bem_presa = 0 #zerar o contador de que não há necessicade de uma mutação
        else: #se o melhor de todos foi bem
            contador_bem_presa += 1 #aumentar o contador que dis respeito a nao ter mutação
        
            if contador_bem_presa >= bem_quantidade_presa: #se chegamos no ponto onde nao era para ter mutação pelo tempo definido
                index_mutacao_presa = 0 #zerar a mutação

                contador_bem_presa = 0 #zerar o contador de que não há necessidade de uma mutação

        #atuailizar a variável referente ao fintess do melhor da geração
        melhor_presa_fitness_geracao_anterior = populacao[0].quantidade

        #---------------------Passar melhores---------------------

        #passar o melhor de todos
        nova_populacao.append(self.AdicionarIndividuo(gene=melhor_de_todos_presa.gene, mapeamento=self.mapeamento_presa, tipo=3))
        nova_populacao.append(self.AdicionarIndividuo(gene=mutate(melhor_de_todos_presa.gene, mutacao_variada_presa[index_mutacao_presa]), mapeamento=self.mapeamento_presa, tipo=3)) #mutacao

        #atualizar o melhor de todos global (se necessário)
        if populacao[0].quantidade >= melhor_de_todos_presa.quantidade:
            melhor_de_todos_presa = copy(populacao[0])

        #Adicionar os melhores
        for i in range(5):
            media_populacao += populacao[i].quantidade #cálculo da média da população

            nova_populacao.append(self.AdicionarIndividuo(gene=populacao[i].gene, mapeamento=self.mapeamento_presa, tipo=3))
            nova_populacao.append(self.AdicionarIndividuo(gene=mutate(populacao[i].gene, mutacao_variada_presa[index_mutacao_presa]), mapeamento=self.mapeamento_presa, tipo=3))

        #---------------------Cruzamento---------------------
        
        #cruzar a melhor metade da população com o melhor da geraçãoW
        for i in range(5, int(len(populacao)/2)):
            media_populacao += populacao[i].quantidade #cálculo da média da população

            nova_populacao.append(self.AdicionarIndividuo(gene=cruzamento(populacao[0], populacao[i]), mapeamento=self.mapeamento_presa, tipo=3))

        #matar a pior metade da população e colocar indivíduos totalmente novos
        for i in range(int(len(populacao)/2), len(populacao) - 7):
            media_populacao += populacao[i].quantidade

            nova_populacao.append(self.AdicionarIndividuo(gene=self.gene_presa, mapeamento=self.mapeamento_presa, tipo=3))

        #obs: o -7 é necessário, pois foi adicionado o melhor de todos, 
        #mutação do melhor de todos e os 5 melhores + mutação dos 5 melhores
    
        print("Presa: ", populacao[0].gene)

        media_populacao /= len(populacao) - 7 #terminar o cálculo da média da população

        #---------------------Gráfico---------------------
        grafico_media_presa.append(media_populacao)
        grafico_melhor_presa.append(populacao[0].quantidade)

        return nova_populacao
    
    def nova_populacao_predadores(self, populacao: list[Individuo])-> list[Individuo]:
        #---------------------Globais---------------------
        global melhor_de_todos_predador
        global grafico_melhor_predador
        global melhor_predador_fitness_geracao_anterior
        global grafico_media_predador

        global index_mutacao_predador
        global contador_bem_predador

        #---------------------Ordenacao---------------------
        nova_populacao = [] #lista com os indivíduos da nova população
        media_populacao = 0 #variável para o cáculo da média da população

        populacao = Ordernar(populacao) #ordernar a população atual
        
        #---------------------Mutação Variada---------------------
        #se o melhor de todos teve um desempenho muito ruim
        if (abs(populacao[0].quantidade)) <= (abs(melhor_predador_fitness_geracao_anterior) / 2):
            #aumentar o index da taxa de mutação
            index_mutacao_predador = (index_mutacao_predador + 1) % len(mutacao_variada_predador) 

            if index_mutacao_predador == 0: #ter certeza que a necessidade de uma mutação variada nao leve a 0 de mutação
                index_mutacao_predador = 1

            contador_bem_predador = 0 #zerar o contador de que não há necessicade de uma mutação
        else: #se o melhor de todos foi bem
            contador_bem_predador += 1 #aumentar o contador que dis respeito a nao ter mutação
        
            if contador_bem_predador >= bem_quantidade_predador: #se chegamos no ponto onde nao era para ter mutação pelo tempo definido
                index_mutacao_predador = 0 #zerar a mutação

                contador_bem_predador = 0 #zerar o contador de que não há necessidade de uma mutação

        #atuailizar a variável referente ao fintess do melhor da geração
        melhor_predador_fitness_geracao_anterior = populacao[0].quantidade

        #---------------------Passar melhores---------------------

        #passar o melhor de todos
        nova_populacao.append(self.AdicionarIndividuo(gene=melhor_de_todos_predador.gene, mapeamento=self.mapeamento_predador, tipo=4))
        nova_populacao.append(self.AdicionarIndividuo(gene=mutate(melhor_de_todos_predador.gene, mutacao_variada_predador[index_mutacao_predador]), mapeamento=self.mapeamento_predador, tipo=4)) #mutacao

        #atualizar o melhor de todos global (se necessário)
        if populacao[0].quantidade >= melhor_de_todos_predador.quantidade:
            melhor_de_todos_predador = copy(populacao[0])

        #Adicionar os melhores
        for i in range(5):
            media_populacao += populacao[i].quantidade #cálculo da média da população

            nova_populacao.append(self.AdicionarIndividuo(gene=populacao[i].gene, mapeamento=self.mapeamento_predador, tipo=4))
            nova_populacao.append(self.AdicionarIndividuo(gene=mutate(populacao[i].gene, mutacao_variada_predador[index_mutacao_predador]), mapeamento=self.mapeamento_predador, tipo=4))

        #---------------------Cruzamento---------------------
        
        #cruzar a melhor metade da população com o melhor da geraçãoW
        for i in range(5, int(len(populacao)/2)):
            media_populacao += populacao[i].quantidade #cálculo da média da população

            nova_populacao.append(self.AdicionarIndividuo(gene=cruzamento(populacao[0], populacao[i]), mapeamento=self.mapeamento_predador, tipo=4))

        #matar a pior metade da população e colocar indivíduos totalmente novos
        for i in range(int(len(populacao)/2), len(populacao) - 7):
            media_populacao += populacao[i].quantidade

            nova_populacao.append(self.AdicionarIndividuo(gene=self.gene_predador, mapeamento=self.mapeamento_predador, tipo=4))

        #obs: o -7 é necessário, pois foi adicionado o melhor de todos, 
        #mutação do melhor de todos e os 5 melhores + mutação dos 5 melhores
    
        print("Predador: ", populacao[0].gene)

        media_populacao /= len(populacao) - 7 #terminar o cálculo da média da população

        #---------------------Gráfico---------------------
        grafico_media_predador.append(media_populacao)
        grafico_melhor_predador.append(populacao[0].quantidade)

        return nova_populacao
    
    def SimulatePresa(self, i: int):
        if i >= len(self.presas): return #nao existe essa presa

        retorno = self.mapa.surroundings(self.presas[i].posicao, 3, tipo=3) #pegar os inputs da presa
                
        inputs = str(retorno[1]) + str(retorno[3]) + str(retorno[5]) #transformar no input necessário para fazer uma ação
        acao = self.presas[i].gene[self.mapeamento_presa[inputs]] #pegar a ação

        #fazer a ação
        nova_posicao, resultado = self.mapa.make_action(action=acao, postion=self.presas[i].posicao, tem_comida=retorno[1], comida=retorno[2], tem_aliado=retorno[3], aliado=retorno[4], tem_inimigo=retorno[5], inimigo=retorno[6], individuo_tipo=3)
        self.presas[i].posicao = nova_posicao #atualizar a posição do indivíduo

        if resultado < 0: #se comeu
            self.presas[i].quantidade += 2
        else: #se não comeu
            self.presas[i].quantidade -= 0.5

    
    def SimulatePredador(self, i):
        if i >= len(self.predadores): return #nao existe esse predador

        retorno = self.mapa.surroundings(self.predadores[i].posicao, 3, tipo=4) #pegar os inputs do predador

        inputs = str(retorno[1]) + str(retorno[3]) #transformar no input necessário para fazer uma ação
        acao = self.predadores[i].gene[self.mapeamento_predador[inputs]] #pegar a ação

        #fazer a ação
        nova_posicao, resultado = self.mapa.make_action(action=acao, postion=self.predadores[i].posicao, tem_comida=retorno[1], comida=retorno[2], tem_aliado=retorno[3], aliado=retorno[4], individuo_tipo=4)
        self.predadores[i].posicao = nova_posicao #atualizar a posição do indivíduo

        if resultado < 0: #se comeu
            self.predadores[i].quantidade += 10

        if resultado == 0.1: #se fez uma ação inválida
            self.predadores[i].quantidade -= 0.5


    def Simulate(self) -> None:
        #---------------------Tamanho---------------------
        if len(self.presas) > len(self.predadores): tamanho = len(self.presas)
        else: tamanho = len(self.predadores)

        #---------------------Simulação---------------------
        for _ in range(self.numero_de_acoes): #para cada ação
            for i in range(tamanho): #para cada presa e predador

                #---------------------Spawn de presas mortas---------------------
                tmp = copy(self.mapa.presas_mortas) #cópia da lista de presas mortas

                for h in range(len(tmp)): #para cada presa morta
                    posicao = self.mapa.posicao_disponivel(3) #pegar uma novoa posição para a presa spawnar

                    for j in range(len(self.presas)):
                        if self.presas[j].posicao == tmp[h]: #achar qual q é a presa q morreu
                            self.presas[j].posicao = posicao #atualizar sua posição

                            self.presas[j].quantidade = 0 #zerar a pontuação dela, pois ela morreu

                            self.mapa.presas_mortas.remove(tmp[h]) #remover da lista de presas mortas

                #---------------------Simulação da rodada---------------------
                self.SimulatePresa(i) #simula somente 1 presa
                self.SimulatePredador(i) #simula somente 1 predador

                

    def StartPopulationPresas(self):
        presas: list[Individuo] = []

        #criar as presas
        for _ in range(self.numero_de_presas):
                posicao = self.mapa.posicao_disponivel(3)

                presas.append(CriarIndividuo(gene=self.gene_presa, posicao=posicao, mapeamento=self.mapeamento_presa, tipo=3))

        return presas
    
    def StartPopulationPredadores(self):
        predadores: list[Individuo] = []

        #criar os predadores
        for _ in range(self.numero_de_predadores):
                posicao = self.mapa.posicao_disponivel(4)

                predadores.append(CriarIndividuo(gene=self.gene_predador, posicao=posicao, mapeamento=self.mapeamento_predador, tipo=4))

        return predadores

    def StartSimulation(self, numero_de_acoes: int, numero_de_presas: int, gene_presa: list, mapeamento_presa: dict,
                        numero_de_predadores: int, gene_predador: list, mapeamento_predador: dict) -> None:
        #---------------------Globais---------------------
        global melhor_de_todos_presa
        global melhor_presa_fitness_geracao_anterior; melhor_presa_fitness_geracao_anterior = -999
        global grafico_media_presa

        global melhor_de_todos_predador
        global melhor_predador_fitness_geracao_anterior; melhor_predador_fitness_geracao_anterior = -999
        global grafico_media_predador

        global contador

        #---------------------Variáveis---------------------
        self.numero_de_acoes: int = numero_de_acoes

        #presa 
        self.numero_de_presas: int = numero_de_presas
        self.gene_presa: list = gene_presa
        self.mapeamento_presa: dict = mapeamento_presa
        self.presas = []

        #predador
        self.numero_de_predadores:int = numero_de_predadores
        self.gene_predador: list = gene_predador
        self.mapeamento_predador: dict = mapeamento_predador
        self.predadores = []

        geracao = 0 

        #---------------------Inicialização---------------------
        self.mapa: Mapa = Mapa(50, 50, obstaculo_chance=0, terra_chance=0.6, grama_chance=0.4) #criar o mapa inicial

        self.presas: list[Individuo] = self.StartPopulationPresas() #cria a população inicial de presas
        self.predadores: list[Individuo] = self.StartPopulationPredadores() #criar a população inicial de predadores

        melhor_de_todos_presa = self.presas[0] #pegar um individuo aleatório para ser o melhor de todos
        melhor_de_todos_predador = self.predadores[0] #pegar um individuo aleatório para ser o melhor de todos

        #---------------------Simular---------------------
        while(True):
            print("Na geração: ", geracao)
            geracao +=1

            #plotagem de gráfico
            if contador == contador_quantidade: 
                contador = 0

                self.Plotar_Grafico()

            contador += 1

            self.Simulate() #fazer uma simulação completa

            self.mapa = Mapa(50, 50, obstaculo_chance=0, terra_chance=0.6, grama_chance=0.4) #criar um novo mapa

            self.presas = self.nova_populacao_presas(self.presas) #pega a nova população de presas
            self.predadores = self.nova_populacao_predadores(self.predadores) #pega a nova população de predadores

           
    def Plotar_Grafico(self) -> None:
        global grafico_melhor_presa
        global grafico_media_presa

        global grafico_media_predador
        global grafico_melhor_predador

        global numero_do_grafico

        # Gerações (assumindo que cada elemento nas listas acima corresponde a uma geração)
        geracoes = list(range(1, len(grafico_melhor_presa) + 1))

        nocao_dimensao = [0] * len(geracoes)

        # Criar o gráfico
        #plt.plot(geracoes, grafico_melhor_presa, label='Melhor presa')
        plt.plot(geracoes, grafico_media_presa, label='Média presa')
        #plt.plot(geracoes, grafico_melhor_predador, label='Melhor predador')
        plt.plot(geracoes, grafico_media_predador, label='Média predador')
        plt.plot(geracoes, nocao_dimensao, label="")

        # Adicionar legendas e títulos
        plt.xlabel('Geração')
        plt.ylabel('Fitness')
        plt.title('Evolução do Fitness ao Longo das Gerações')
        plt.legend()

        diretorio = os.path.join("graficos", str(numero_do_grafico) + ".png")

        # Mostrar o gráfico
        plt.savefig(diretorio)
        plt.close()

        numero_do_grafico += 1 #atualizar o numero do grafico