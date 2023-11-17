from ag.ag import AG
from individuos.individuo import CriarIndividuo

import math

ag = AG()

def StartPopulation(numero_de_individuos: int, gene: list):
    individuos = []

    for _ in range(numero_de_individuos):
            individuos.append(CriarIndividuo(gene=gene))

    return individuos

def GetFitness(individuos):
    def criterio_de_ordenacao(individuo):
        posicao_objetivo = individuo.posicao_objetivo

        # Calcula a distância Euclidiana entre a posição do indivíduo e o objetivo
        dx = individuo.posicao[0] - posicao_objetivo[0]
        dy = individuo.posicao[1] - posicao_objetivo[1]
        segundo_criterio = math.sqrt(dx**2 + dy**2)

        return segundo_criterio

    return sorted(individuos, key=criterio_de_ordenacao)

def NewPopulation(fitness: list):
    individuos = []

    individuos.append(CriarIndividuo(fitness[0].network.GetGene())) #colocar o melhor de todos
    individuos.append(CriarIndividuo(ag.mutate(fitness[0].network.GetGene()))) #colocar uma mutação do melhor de todos

    for i in range(1, len(fitness) - 1):
        individuos.append(CriarIndividuo(ag.mutate(fitness[i].network.GetGene())))

    return individuos

class Simulacao():
    def __init__(self) -> None:
        pass

    def Simulate(self):
        for individuo in self.individuos:
            for passo in range(self.numero_de_passos):
                if not(individuo.objetivo_concluido):
                    individuo.numero_de_passos += 1 #aumentar o número de passos em 1

                    inputs = individuo.mapa.inputs(individuo.posicao) #pegar os inputs para esse individuo

                    predicao = individuo.network.predict(inputs) #fazer a predicao

                    #ver qual ação deve ser feita
                    acao = predicao.index(max(predicao)) + 1 #mais 1 só pra eu n ter q mexer no codigo do mapa

                    #fazer a ação e pegar a nova posição do indivíduo após a ação
                    nova_posicao = individuo.mapa.make_action(acao, individuo.posicao)
                    individuo.posicao = nova_posicao    

                    #se o indivíduo chegou no objetivo
                    if individuo.posicao == individuo.posicao_objetivo:
                        individuo.objetivo_concluido = True

    def StartSimulation(self, numero_de_geracoes: int, numero_de_individuos: int, numero_de_passos: int, gene_individuo: list):
        self.numero_de_geracoes = numero_de_geracoes
        self.numero_de_indivudos = numero_de_individuos
        self.numero_de_passos = numero_de_passos

        self.individuos = StartPopulation(numero_de_individuos, gene=gene_individuo)

        for geracao in range(self.numero_de_geracoes):
            print(f"Na geração {geracao}")

            self.Simulate()
    
            self.fitness = GetFitness(self.individuos)

            self.individuos = NewPopulation(self.fitness)
    
    def Results(self):
        for individuo in self.fitness:
            print(f"{individuo.objetivo_concluido}, {individuo.numero_de_passos}, {math.sqrt((individuo.posicao[0] - individuo.posicao_objetivo[0])**2 + (individuo.posicao[1] - individuo.posicao_objetivo[1])**2)}")
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