import numpy as np
from activation_functions import Tanh
from loss import MSE
from classes import DenseLayer

def get_loss_function(loss_function):
    functions = {
        "MSE": MSE
    }

    if loss_function not in functions.keys():
        return None
    
    return functions[loss_function]

def get_activation_function(activation_function):
    functions = {
        "Tanh": Tanh
    }

    if activation_function not in functions.keys():
        return None
    
    return functions[activation_function]

class Dense:
    def __init__(self, number_of_inputs, activation_function, input_shape: list = None) -> None:
        self.number_of_inputs = number_of_inputs
        self.activation_function = get_activation_function(activation_function)

        self.input_shape = input_shape

        if self.activation_function == None:
            print("Invalid activation function!")
            return None
        
class Network:
    def __init__(self, model_strucutre: int):
        self.model = []

        number_of_inputs = model_strucutre[0].number_of_inputs

        #adicionar todas as layers menos a ultima
        for i in range(0, len(model_strucutre) - 1):
            self.model.append(DenseLayer(number_of_inputs, model_strucutre[i + 1].number_of_inputs)) #adicionar a layer
            self.model.append(model_strucutre[i].activation_function()) #adicionar a funcao de ativacao

            number_of_inputs = model_strucutre[i + 1].number_of_inputs
        
        self.model.append(DenseLayer(model_strucutre[-1].number_of_inputs, model_strucutre[-1].number_of_inputs,))
        self.model.append(model_strucutre[-1].activation_function())

        self.input_shape = model_strucutre[0].input_shape
        self.output_shape = model_strucutre[-1].input_shape

    def predict(self, input):
        prediction = input

        for layer in self.model:
            prediction = layer.forward(prediction)

        return prediction
    
    def train(self, inputs, outputs, learning_rate: float, loss_function: str, epochs: int, verbose: bool = True):
        inputs = np.reshape(inputs, self.input_shape)
        outputs = np.reshape(outputs, self.output_shape)

        loss = get_loss_function(loss_function)

        if loss == None:
            print("Invalid loss function!")
            return None

        loss = loss()

        for epoch in range(0, epochs):
            erro = 0

            for input, output in zip(inputs, outputs):
                predicted = self.predict(input)

                erro += loss.calculate(output, predicted)

                gradient = loss.gradient(output, predicted)

                for layer in reversed(self.model):
                    gradient = layer.backward(gradient, learning_rate)

            erro = erro / len(inputs)

            if verbose:
                print(f"Epoch: {epoch}. Loss: {erro}")
            

    def architecture(self):
        contador = 0

        for layer in self.model:
            if layer.type == "dense":
                print(f"Layer: {contador}")

                print(f"Neuronios de input: {layer.input_size}")
                print(f"Neuronios de output: {layer.output_size}")

                contador += 1
            else:
                print(f"Função de ativação: Tanh")

                print()