import random
import numpy as np

def mutate_weihts(gene):
    numero_de_camadas = len(gene)
    camada_sorteada = random.randint(0, numero_de_camadas - 1)

    peso_shape = gene[camada_sorteada]["weights_shape"]

    a = random.randint(0, peso_shape[0] - 1)
    b = random.randint(0, peso_shape[1] - 1)

    gene[camada_sorteada]["weights"][a][b] = np.random.randn()

    return gene


def mutate_bias(gene):
    numero_de_camadas = len(gene)
    camada_sorteada = random.randint(0, numero_de_camadas - 1)

    bias_shape = gene[camada_sorteada]["bias_shape"]

    a = random.randint(0, bias_shape[0] - 1)
    b = random.randint(0, bias_shape[1] - 1)

    gene[camada_sorteada]["bias"][a][b] = np.random.randn()

    return gene


class AG:
    def __init__(self) -> None:
        pass   
    
    def mutate(self, gene, qtd_mutacoes: int):
        gene = gene

        for i in range(qtd_mutacoes):
            dice = random.randint(0, 1)

            if dice == 1:
                print("a")
                gene = mutate_weihts(gene)
            
            if dice == 0:
                print("b")
                gene =  mutate_bias(gene)

        return gene