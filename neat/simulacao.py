from NeuralNetowrk.NeuralNetwork import NeuralNetwork
from mapa import Mapa
from ag.ag import AG

import math

numero_de_geracoes = 1000
numero_de_individuos = 100
numero_de_passos = 30

ag = AG()

class Individuo:
    def __init__(self, network: NeuralNetwork, posicao: list, mapa: Mapa, posicao_objetivo: list, gene: list) -> None:
        self.objetivo_concluido = False
        self.numero_de_passos = 0

        self.network = network
        self.network.CreateNetwrok(gene=gene)

        self.posicao = posicao
        self.posicao_objetivo = posicao_objetivo

        self.mapa = mapa

def ordena_individuos(individuos):
    def criterio_de_ordenacao(individuo):
        posicao_objetivo = individuo.posicao_objetivo

        # Calcula a distância Euclidiana entre a posição do indivíduo e o objetivo
        dx = individuo.posicao[0] - posicao_objetivo[0]
        dy = individuo.posicao[1] - posicao_objetivo[1]
        segundo_criterio = math.sqrt(dx**2 + dy**2)

        return segundo_criterio

    return sorted(individuos, key=criterio_de_ordenacao)

def cirar_individuo(gene):
    mapa = Mapa(4, 4, obstaculo_chance=0, terra_chance=1, grama_chance=0)

    mapa.mapa[3][3] = 1
    posicao_objetivo = (3, 3)

    posicao = (0, 0)
    mapa.mapa[0][0] = 2

    return Individuo(NeuralNetwork(), posicao=posicao, mapa=mapa, posicao_objetivo=posicao_objetivo, gene=gene) #criar o individuo

"""
será passado quatro inputs:
se tem o objetivo em cima
se tem o objetivo em baixo
se tem o objetivo na esquerda
se tem o objetivo na direita

os outputs vão ser:
ir pra cima
ir pra baixo
ir pra esquerda
ir pra direita
"""
gene = [[[[0, 0], [4, None], [5, None], [6, None], [7, None]], [[1, 0], [4, None], [5, None], [6, None], [7, None]], [[2, 0], [4, None], [5, None], [6, None], [7, None]], [[3, 0], [4, None], [5, None], [6, None], [7, None]]],
        [[[4, None]], [[5, None]], [[6, None]], [[7, None]]]]

individuos = []

for _ in range(numero_de_individuos):
        individuos.append(cirar_individuo(gene=gene))

for i in range(numero_de_geracoes):
    print(f"Na geracao: {i}")
    
    for individuo in individuos:
        for passo in range(numero_de_passos): #tem 7 passos para conseguir chegar no objetivo
            if not(individuo.objetivo_concluido):
                individuo.numero_de_passos += 1

                inputs = individuo.mapa.inputs(individuo.posicao)

                predicao = individuo.network.predict(inputs)

                acao = predicao.index(max(predicao)) + 1 #mais 1 só pra eu n ter q mexer no codigo do mapa

                nova_posicao = individuo.mapa.make_action(acao, individuo.posicao)

                individuo.posicao = nova_posicao    

                if individuo.posicao == individuo.posicao_objetivo:
                    individuo.objetivo_concluido = True

    fitness = ordena_individuos(individuos)

    individuos = []

    individuos.append(cirar_individuo(fitness[0].network.GetGene())) #colocar o melhor de todos
    individuos.append(cirar_individuo(ag.mutate(fitness[0].network.GetGene()))) #colocar uma mutação do melhor de todos

    for i in range(1, len(fitness) - 1):
        individuos.append(cirar_individuo(ag.mutate(fitness[i].network.GetGene())))

for individuo in fitness:
    print(f"{individuo.objetivo_concluido}, {individuo.numero_de_passos}, {math.sqrt((individuo.posicao[0] - individuo.posicao_objetivo[0])**2 + (individuo.posicao[1] - individuo.posicao_objetivo[1])**2)}")