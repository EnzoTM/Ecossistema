from simulacao import Simulacao
from NeuralNetowrk.NeuralNetwork import Dense

modelo = [
    Dense(4, activation_function="Tanh", input_shape=(4,)),
    Dense(5, activation_function="Tanh", input_shape=(1,))
]


simulacao = Simulacao()

simulacao.StartSimulation(numero_de_acoes=100, numero_de_individuos=50,  modelo=modelo)