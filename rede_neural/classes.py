import numpy as np

class Dense:
    def __init__(self, input_size, output_size) -> None:
        self.weights = np.random.randn(output_size, input_size) #inicializar randomicamente os pesos
        self.bias = np.random.randn(output_size, 1) #inicializar randomicamente os bias

    def forward(self, input):
        self.input = input

        #calcular o output que deverá ser passado como input para o próximo neuronio (te amo NUMPY <3)
        return np.dot(self.weights, self.input) + self.bias 
    
    def backward(self, gradiente, learning_rate = 1):
        weights_gradiente = np.dot(gradiente, self.input.T) #calcular o gradiente dos pesos
        inputs_gradiente = np.dot(self.weights.T, gradiente) #calcular o gradiente dos inputs
        weights_bias = gradiente #"calcular" o gradiente dos bias

        self.weights = self.weights - (weights_gradiente * learning_rate) #fazer as devidas mudanças nos pesos
        self.bias = self.bias - (weights_bias * learning_rate) #fazer as devidas mudanças nos bias

        #retornar o gradiente do input, que servirá como o gradiente de entrada para o neuronio anterior
        return inputs_gradiente
    
class Activation:
    def __init__(self, activation, derivada):
        self.activation = activation
        self.derivada = derivada

    def forward(self, input):
        self.input = input

        #retornar o valor do resultado da função de ativação
        return self.activation(self.input)
    
    def backward(self, gradiente, learning_rante):
        #retornar o gradiente da função de ativação
        return np.multiply(gradiente, self.derivada(self.input))