from NeuralNetowrk.NeuralNetwork import NeuralNetwork
from mapa.mapa import Mapa

def CriarIndividuo(gene, posicao):
        return Individuo(NeuralNetwork(), posicao=posicao, gene=gene) #criar o individuo

class Individuo:
    def __init__(self, network: NeuralNetwork, posicao: list, gene: list) -> None:
        self.network = network
        self.network.CreateNetwrok(gene=gene)

        self.posicao = posicao
        self.vivo = True
        self.fome = 0