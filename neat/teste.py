from ag.ag import AG
from NeuralNetowrk.NeuralNetwork import NeuralNetwork
from mapa import Mapa
"""
gene = [
    [[[0, 0], [2, 0.3]], [[1, 0], [2, 0.2]]],
    [[[2, 0], [3, 2]]],
    [[[3, 0]]]
]

ag = AG()

nn = NeuralNetwork()
nn.CreateNetwrok(gene)

nn.GetGene()"""

mapa = Mapa(4, 4, obstaculo_chance=0, terra_chance=1, grama_chance=0)

posicao_objetivo = mapa.posicao_disponivel(1)

posicao = mapa.posicao_disponivel(2) #o individuo vai ser reconhecido por um 2

mapa.printar_mapa()

print(mapa.inputs(posicao))