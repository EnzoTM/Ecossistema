import numpy as np
from rede_neural.rede_neural import Network
from mapa import Mapa


def get_list_given_a_shape(shape):
    return np.random.randn(shape[0], shape[1])

def create_gene(model_architecture, shapes):
    """
    o gene terá meio que a mesma arquitetura que a lista de shapes da rede neural (funcao get_shapes() da rede neural)
    """
    genes = []

    #para cada uma das layers
    for i in range(len(model_architecture)):
        genes.append([get_list_given_a_shape(shapes[i][0]), get_list_given_a_shape(shapes[i][1])])

    return genes

class Younglings:
    def __init__(self, model_architecture: list, espaco: Mapa, alcance: int, posicao: list, shapes: list, fome: int = 0, vida: int = 1, gene: list = None):
        #criar o gene se ele nao foi fornecido
        if gene == None:
            self.gene = create_gene(model_architecture, shapes)
        else:
            self.gene = gene
        
        #criação da rede neural
        self.rede_neural = Network()
        self.rede_neural.create_model(model_architecture, gene=self.gene)
        
        #criação dos parametos
        self.fome = fome
        self.vivo = True
        self.vida = vida
        self.alcance = alcance #alcance de visão
        self.posicao = posicao
        self.surroundings = espaco.surroundings(posicao, alcance) 

        #adicionar as informações pertinentes aos sensores  
        self.sensores = []
        self.sensores.append(self.fome)

        for i in range(alcance):
            for j in range(alcance):
                self.sensores.append(self.surroundings[i][j])

    def action(self):
        """
        pega qual ação deve ser feita
        """
        lista = self.rede_neural.predict(self.sensores).tolist() #pegar a predicao da rede neural

        action = lista.index(max(lista)) #pegar a ação que a rede neural disse que era para fazer

        return action