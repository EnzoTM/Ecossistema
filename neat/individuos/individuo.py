from NeuralNetowrk.NeuralNetwork import NeuralNetwork

def CriarIndividuo(gene, posicao, tipo):
        return Individuo(NeuralNetwork(), posicao=posicao, gene=gene, tipo=tipo) #criar o individuo

class Individuo:
    def __init__(self, network: NeuralNetwork, posicao: list, gene: list, tipo: int) -> None:
        self.network = network
        self.network.CreateNetwrok(gene=gene)

        self.posicao = posicao
        self.vida = 1
        self.fome = 0

        self.gene = self.network.GetGene()

        self.tipo = tipo