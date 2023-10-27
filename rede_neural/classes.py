import numpy as np

class Activation:
    def __init__(self, function, gradiente, name):
        self.function = function #armazenar a função em si
        self.gradiente = gradiente #armazenar o gradiente da função
        self.name = name

    def forward(self, input):
        self.input = input #armazenar o input, pois o utilizare-mos no backpropagation 

        #retornar o valor do resultado da função de ativação
        return self.function(self.input)
    
    def backward(self, gradiente):
        #retornar o gradiente da função de ativação
        return np.multiply(gradiente, self.gradiente(self.input))

class DenseLayer:
    def __init__(self, input_size: int, output_size: int, activation_function: Activation, weights: np.array = None, bias: np.array = None):
        self.activation_function = activation_function() #pegar a função de ativação

        if weights is None and bias is None:
            self.weights = np.random.randn(output_size, input_size) #inicializar randomicamente os pesos
            self.bias = np.random.randn(output_size, 1) #inicializar randomicamente os bias
        else:
            self.weights = weights
            self.bias = bias

        self.input_size = input_size #guardar quantos inputs tem (número de neuronios da camada)
        self.output_size = output_size #guardar quantos outputs tem (número de neuronios da próxima camada)

    def forward(self, input):
        self.input = input #guardar o input, pois usaremos ele na hora de calcular o backpropagation

        #np.dot(self.weights, self.input) + self.bias calcula o output que deverá ser passado como input para o próximo neuronio
        #depois passamos isso para a função de ativação
        return self.activation_function.forward(np.dot(self.weights, self.input) + self.bias)

    
    def backward(self, gradiente, learning_rate):
        #calcular o gradiente da função de ativação
        gradiente = self.activation_function.backward(gradiente)

        weights_gradiente = np.dot(gradiente, self.input.T) #calcular o gradiente dos pesos
        inputs_gradiente = np.dot(self.weights.T, gradiente) #calcular o gradiente dos inputs
        weights_bias = gradiente #"calcular" o gradiente dos bias

        self.weights = self.weights - (weights_gradiente * learning_rate) #fazer as devidas mudanças nos pesos
        self.bias = self.bias - (weights_bias * learning_rate) #fazer as devidas mudanças nos bias

        #retornar o gradiente do input, que servirá como o gradiente de entrada para a função de ativação do neuronio anterior
        return inputs_gradiente