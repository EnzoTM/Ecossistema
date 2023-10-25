from .classes import Activation
import numpy as np

class Tanh(Activation):
    def __init__(self):
        tanh = lambda x: np.tanh(x) #criar a função tangente hiperbólica

        derivada = lambda x: 1 - (np.tanh(x) ** 2) #criar função da derivada da tangente hiperbólica

        super().__init__(tanh, derivada, "Tanh")


class Sigmoid(Activation):
    def __init__(self):
        sigmoid = lambda x: 1 / (1 + np.exp(-x)) # sigmoid function

        derivative = lambda x: sigmoid(x) * (1 - sigmoid(x)) # derivative of the sigmoid function

        super().__init__(sigmoid, derivative, "Sigmoid")


class ReLU(Activation):
    def __init__(self):
        relu = lambda x: np.maximum(0, x)  # ReLU function

        derivative = lambda x: np.where(x > 0, 1, 0)  # derivative of the ReLU function

        super().__init__(relu, derivative, "ReLU")