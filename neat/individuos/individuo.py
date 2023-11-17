from NeuralNetowrk.NeuralNetwork import NeuralNetwork
from mapa.mapa import Mapa

def CriarIndividuo(gene):
        mapa = Mapa(10, 10, obstaculo_chance=0, terra_chance=1, grama_chance=0)

        posicao_objetivo = mapa.posicao_disponivel(1)
        posicao = mapa.posicao_disponivel(2)

        return Individuo(NeuralNetwork(), posicao=posicao, mapa=mapa, posicao_objetivo=posicao_objetivo, gene=gene) #criar o individuo

class Individuo:
    def __init__(self, network: NeuralNetwork, posicao: list, mapa: Mapa, posicao_objetivo: list, gene: list) -> None:
        self.objetivo_concluido = False
        self.numero_de_passos = 0

        self.network = network
        self.network.CreateNetwrok(gene=gene)

        self.posicao = posicao
        self.posicao_objetivo = posicao_objetivo

        self.mapa = mapa