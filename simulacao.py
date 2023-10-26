from objetos.mapa import Mapa
from objetos.younglings import Younglings

from rede_neural.rede_neural import Network, Dense, get_shapes

"""
sensores do padawan:
*fome
*ao redor (alcance de 5) 5*5

Logo teremos 26 sensores

Ações:
*cima
*direita
*esquerda
*abaixo
*comer
"""

numero_de_padawans = 5

padawan_rede_neural = [
    Dense(26, input_shape=(26, 1), activation_function="ReLU"), #sensores
    Dense(5, activation_function="Sigmoid", input_shape=(5, 1))
]

padawan_rede_neural_shapes = get_shapes(padawan_rede_neural)

espaco = Mapa(10, 10)   

padawan = Younglings(padawan_rede_neural, espaco, 5, espaco.posicao_disponivel(4), padawan_rede_neural_shapes)

print(padawan.rede_neural.predict(padawan.sensores))

"""
for i in range(len(padawans)):
    for layer in padawans[i].rede_neural.model:
        print(f"Weights: {layer.weights}. \nBias: {layer.bias}")

    print()
    print()"""