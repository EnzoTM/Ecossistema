from classes import Activation
import numpy as np

class Tanh(Activation):
    def __init__(self):
        tanh = lambda x: np.tanh(x) #criar a função tangente hiperbólica

        derivada = lambda x: 1 - (np.tanh(x) ** 2) #criar função da derivada da tangente hiperbólica

        super().__init__(tanh, derivada, "Tanh")