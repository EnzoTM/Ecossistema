from ag.ag import AG
from individuos.individuo import CriarIndividuo, Individuo
from mapa.mapa import Mapa

import math
import random

ag = AG()

def melhor_individuo(individuo1: Individuo, individuo2: Individuo):
    if individuo1.vida > individuo2.vida:
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

def comparar_estrutura():
    #TODO
    return


def separar_em_especies(populacao):
    lista_subespecies = []

    for individuo in populacao:
        flag = False  # Indica se encontrou uma subespécie correspondente

        for subespecie in lista_subespecies:
            if comparar_estrutura(subespecie[0].gene, individuo.gene):
                subespecie.append(individuo)
                flag = True
                break

        if not flag:
            lista_subespecies.append([individuo])
        
    return lista_subespecies

class Simulacao():
    def __init__(self) -> None:
        pass

    def torneio_de_dois(self, populacao: list[Individuo], tipo: int)->list:
        nova_populacao: list = []

        melhor: Individuo = populacao[0]

        #pegar o melhor indivíduo
        for i in range(0, len(populacao)): 
            if populacao[i].vida > melhor.vida:
                melhor = populacao[i]
        
        nova_populacao.append(melhor) #colcoar o melhor de todos na proxima geração

        for _ in populacao:
            pai1 = melhor_individuo(populacao[random.randint(0, len(populacao) - 1)], populacao[random.randint(0, len(populacao) - 1)])
            pai2 = melhor_individuo(populacao[random.randint(0, len(populacao) - 1)], populacao[random.randint(0, len(populacao) - 1)])

            gene = cruzamento(pai1, pai2)

            gene = ag.mutate(gene) #mutar o gene

            posicao = self.mapa.posicao_disponivel(tipo)

            filho = CriarIndividuo(gene=gene, posicao=posicao, tipo=tipo)

            nova_populacao.append(filho)
        
        return nova_populacao
    
    def StartPopulation(self, numero_de_individuos: int, gene: list):
        individuos = []

        posicao = self.mapa.posicao_disponivel(3)

        for _ in range(numero_de_individuos):
                individuos.append(CriarIndividuo(gene=gene, posicao=posicao, tipo=3))

        return individuos

    def Simulate(self):
        for _ in range(self.numero_de_acoes):
            for individuo in self.individuos:
                if (individuo.vida > 0):
                    individuo.fome += 0.1 #aumentar a fome

                    inputs = self.mapa.inputs(individuo.posicao) #pegar os inputs para esse individuo

                    predicao = individuo.network.predict(inputs) #fazer a predicao

                    #ver qual ação deve ser feita
                    acao = predicao.index(max(predicao))

                    #fazer a ação e pegar a nova posição do indivíduo após a ação
                    nova_posicao, resultado = self.mapa.make_action(acao, individuo.posicao)
                    individuo.posicao = nova_posicao   


                    individuo.fome += resultado

                    if individuo.fome > 1: individuo.fome = 1
                    if individuo.fome < 0: individuo.fome = 0

                    #se o indivíduo está com fome
                    if individuo.fome == 1:
                        individuo.vida -= 0.1

                        if individuo.vida == 0: #se o individuo morreu
                            self.mapa[individuo.posicao[0], individuo.posicao[1]] = 0 #deixar aquela posicao como disponível
            

    def StartSimulation(self, numero_de_geracoes: int, numero_de_individuos: int, numero_de_acoes: int, gene_individuo: list):
        self.numero_de_geracoes = numero_de_geracoes
        self.numero_de_indivudos = numero_de_individuos
        self.numero_de_acoes = numero_de_acoes

        self.mapa = Mapa(50, 50, obstaculo_chance=0, terra_chance=0.75, grama_chance=0.25)

        self.individuos = self.StartPopulation(numero_de_individuos=numero_de_individuos, gene=gene_individuo)

        for geracao in range(self.numero_de_geracoes):
            print(f"Na geração {geracao}")

            self.Simulate()

            self.mapa.atualizar(self.individuos) #atualizar o mapa

            self.individuos = self.torneio_de_dois(self.individuos, self.individuos[0].tipo)
    def Results(self):
        for individuo in self.fitness:
            print(f"{individuo.objetivo_concluido}, {individuo.numero_de_acoes}, {math.sqrt((individuo.posicao[0] - individuo.posicao_objetivo[0])**2 + (individuo.posicao[1] - individuo.posicao_objetivo[1])**2)}")
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