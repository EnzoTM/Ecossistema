from NeuralNetowrk.NeuralNetwork import NeuralNetwork

def CriarIndividuo(gene: list, modelo: list, posicao: tuple, tipo: int):
        return Individuo(NeuralNetwork(), posicao=posicao, gene=gene, tipo=tipo, modelo=modelo) #criar o individuo

class Individuo:
    def __init__(self, network: NeuralNetwork, posicao: list, gene: list, tipo: int, modelo: list) -> None:
        self.network = network

        if gene == None: #criar a partir do modelo
            self.network.CreateNetwrok(model_strucutre=modelo)
        else: #criar apartir do gene
            self.network.CreateNetwrokFromGene(gene=gene)

        self.posicao = posicao
        self.vida = 1
        self.fome = 0

        self.gene = self.network.GetGene()

        self.tipo = tipo

        self.quantidade = 0