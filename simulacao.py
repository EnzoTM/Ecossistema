from objetos.mapa import Mapa
from objetos.younglings import Younglings

from rede_neural.rede_neural import Network, Dense

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
    Dense(52, activation_function="ReLU"),
    Dense(52, activation_function="ReLU"),
    Dense(5, activation_function="Sigmoid", input_shape=(5, 1))
]

espaco = Mapa(10, 10)   

padawans = []

for i in range(numero_de_padawans):
    padawans.append(Younglings(Network(padawan_rede_neural), espaco, 5, espaco.posicao_disponivel(4)))

print(padawans[0].rede_neural.predict(padawans[0].sensores)) 