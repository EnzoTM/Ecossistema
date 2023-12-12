from NeuralNetwork.NeuralNetwork import NeuralNetwork, Dense
from mapa.mapa import Mapa
from individuos.individuo import CriarIndividuo, Individuo
from ag.ag import AG

class Simulacao:
    def __init__(self) -> None:
        pass

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

    def StartPopulation(self):
        nova_populacao: list[Individuo] = []

        for i in range(self.numero_de_individuos): #para cada individuo
            posicao = self.mapa.posicao_disponivel(self.tipos_individuos[i]) #pegar uma nova posição

            nova_populacao.append( #adicionar o novo indivíduo
                CriarIndividuo(posicao=posicao, tipo=self.tipos_individuos[i], #passar a posicao e o tipo
                               gene=self.genes_individuos[i], #passar o gene
                               arquitetura=self.arquitetura_individuos[i]) #passar a arquitetura
                )
            
        return nova_populacao

    def StartSimulation(self, numero_de_geracoes: int, numero_de_acoes: int, numero_de_individuos: int,  genes_individuos: list, arquitetura_individuos: list, tipos_individuos: list):
        self.numero_de_geracoes = numero_de_geracoes
        self.numero_de_acoes = numero_de_acoes
        self.numero_de_individuos = numero_de_individuos
        self.genes_individuos = genes_individuos
        self.arquitetura_individuos = arquitetura_individuos
        self.tipos_individuos = tipos_individuos

        self.mapa = Mapa(50, 50, obstaculo_chance=0, terra_chance=0.50, grama_chance=0.50) #criar o mapa

        self.individuos = self.StartPopulation()

        for i in range(self.numero_de_geracoes):
            print("Na geração: ", i)

            self.Simulate()