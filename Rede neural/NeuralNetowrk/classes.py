import numpy as np

class Activation:
    def __init__(self, function, gradiente, name):
        self.function = function #armazenar a função em si
        self.gradiente = gradiente #armazenar o gradiente da função
        self.name = name

    def forward(self, input):
        #retornar o valor do resultado da função de ativação
        return self.function(input)

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
        #depois passamos isso para a função de ativação
        return self.activation_function.forward(np.dot(self.weights, input) + self.bias)
