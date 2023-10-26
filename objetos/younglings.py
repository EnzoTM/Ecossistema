"""
padawan_rede_neural = [
    Dense(26, input_shape=(26, 1), activation_function="ReLU"), #sensores Weights shape: (52, 26). Bias shape: (52, 1)
    Dense(52, activation_function="ReLU"), Weights shape: (52, 52). Bias shape: (52, 1)
    Dense(52, activation_function="ReLU"), Weights shape: (5, 52). Bias shape: (5, 1)
    Dense(5, activation_function="Sigmoid", input_shape=(5, 1)) Weights shape: (5, 5). Bias shape: (5, 1)
]
"""
import numpy as np
from rede_neural.rede_neural import Network

import random

def get_list_given_a_shape(shape):
    #print(f"Shape: {shape}")
    teste = np.random.randn(shape[0], shape[1])
    #teste = [[random.random() for _ in range(shape[1])] for _ in range(shape[0])]

    #return np.reshape(teste, shape)

    return teste

def create_gene(model_architecture, shapes):
    """W
    o gene terá meio que a mesma arquitetura que a lista de shapes da rede neural (funcao get_shapes() da rede neural)
    """
    genes = []

    #para cada uma das layers
    for i in range(len(model_architecture)):
        genes.append([get_list_given_a_shape(shapes[i][0]), get_list_given_a_shape(shapes[i][1])])

    return genes

class Younglings:
    def __init__(self, model_architecture, espaco, alcance, posicao: list, shapes, fome = 0, vida = 100):
        self.gene = create_gene(model_architecture, shapes)
                
        self.rede_neural = Network()
        self.rede_neural.create_model(model_architecture, gene=self.gene)
        
        
        self.fome = fome
        self.vivo = True
        self.vida = vida
        self.alcance = alcance #alcance de visão
        self.posicao = posicao

        self.surroundings = espaco.surroundings(posicao, alcance) 

        self.sensores = []
        self.sensores.append(self.fome)

        for i in range(alcance):
            for j in range(alcance):
                self.sensores.append(self.surroundings[i][j])

    def action(self):
        lista = self.rede_neural.predict(self.sensores).tolist()

        action = lista.index(max(lista))

        print(action)