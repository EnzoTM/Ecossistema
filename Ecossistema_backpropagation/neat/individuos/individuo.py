from NeuralNetwork.NeuralNetwork import NeuralNetwork

def CriarIndividuo(gene, posicao, arquitetura, tipo):
        return Individuo(NeuralNetwork(), posicao=posicao, gene=gene, tipo=tipo, arquitetura=arquitetura) #criar o individuo

class Individuo:
    def __init__(self, network: NeuralNetwork, posicao: list, gene: list, tipo: int, arquitetura: list) -> None:
        self.network = network

        if gene == None: self.network.CreateNetwrok(model_strucutre=arquitetura) #criar a network baseada na arquitetura (pesos e bias randomicos)
        else: self.network.CreateNetwrokFromGene(gene) #criar a network baseada no gene dado (pesos e bias já definidos)

        self.posicao = posicao
        self.vida = 1
        self.fome = 0

        self.gene = self.network.GetGene()

        self.tipo = tipo

        self.quantidade = 0