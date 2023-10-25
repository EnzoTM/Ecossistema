from .activation_functions import Tanh, Sigmoid, ReLU
from .loss import MSE
from .classes import DenseLayer

import json
import numpy as np

def get_loss_function(loss_function):
    functions = {
        "MSE": MSE
    }

    if loss_function not in functions.keys():
        return None
    
    return functions[loss_function]

def get_activation_function(activation_function):
    functions = {
        "Tanh": Tanh,
        "Sigmoid": Sigmoid,
        "ReLU": ReLU
    }

    if activation_function not in functions.keys():
        return None
    
    return functions[activation_function]

class Dense: #classe para a construção da arquitetura do modelo pelo usuário
    def __init__(self, number_of_inputs, activation_function, input_shape: list = None) -> None:
        self.number_of_inputs = number_of_inputs #guardar o número de inputs
        self.activation_function = get_activation_function(activation_function) #pegar a função de ativação (função em si, ainda tem que "ativa-la")

        self.input_shape = input_shape #guardar o shape do input (só será usado na primeira e última camada)

        #fazer checagem de erro
        if self.activation_function == None:
            print("Invalid activation function!")
            return None
        
class Network:
    def __init__(self, model_strucutre: int):
        self.model = []

        if model_strucutre != []:
            #adicionar todas as layers menos a ultima
            for i in range(0, len(model_strucutre) - 1):
                #a quantidade de  inputs será a quantidade de outputs da ultima camada e a quantidade de output será a quantidade de inputs da próxima camada
                self.model.append(DenseLayer(model_strucutre[i].number_of_inputs, model_strucutre[i + 1].number_of_inputs, model_strucutre[i].activation_function)) #adicionar a layer
            
            #adicionar a última camda (camda de output). Os números de inputs dela serão os mesmos números de output (que irão passar pela sua função de ativação)
            self.model.append(DenseLayer(model_strucutre[-1].number_of_inputs, model_strucutre[-1].number_of_inputs, model_strucutre[-1].activation_function))

            self.input_shape = model_strucutre[0].input_shape #armazenar o shape dos inputs (sendo utilizado na hora do treinamento)
            self.output_shape = model_strucutre[-1].input_shape #armazenar o shape dos otuputs (sendo utilizado na hora do treinamento)

    def predict(self, input):
        prediction = np.reshape(input, self.input_shape)

        #"andar" pela rede neural para calcular a predição
        for layer in self.model:
            prediction = layer.forward(prediction)

        return prediction
    
    def train(self, inputs, outputs, learning_rate: float, loss_function: str, epochs: int, verbose: bool = True):
        inputs = np.reshape(inputs, self.input_shape) #transformar os inputs em um np.array com o shape correto
        outputs = np.reshape(outputs, self.output_shape)#transformar os otuputs em um np.array com o shape correto

        loss = get_loss_function(loss_function) #pegar a função de perda
        
        #tratar erro
        if loss == None:
            print("Invalid loss function!")
            return None

        loss = loss() #inicializar a função loss

        #fazer o treinamento para cada epoch
        for epoch in range(0, epochs):
            erro = 0

            #para cada dupla de input output
            for input, output in zip(inputs, outputs):
                predicted = self.predict(input) #ver o valor que a IA está predizindo

                erro += loss.calculate(output, predicted) #calcular o erro da IA

                gradient = loss.gradient(output, predicted) #calcular o vetor gradiente

                #fazer o algorítimo de backpropagation
                for layer in reversed(self.model):
                    gradient = layer.backward(gradient, learning_rate)

            erro = erro / len(inputs) #tirar a média do erro

            if verbose:
                print(f"Epoch: {epoch}. Loss: {erro}")

    def save(self):
        model_architecture = []

        for layer in self.model:
            layer_dict = {}

            layer_dict["input_size"] = layer.input_size
            layer_dict["output_size"] = layer.output_size

            layer_dict["weights"] = layer.weights.tolist()
            layer_dict["weights_shape"] = list(layer.weights.shape)

            layer_dict["bias"] = layer.bias.tolist()
            layer_dict["bias_shape"] = list(layer.bias.shape)

            layer_dict["activation_function"] = layer.activation_function.name

            model_architecture.append(layer_dict)

        with open("model.json", "w") as f:
            json.dump(model_architecture, f)
    
    def open_model(self):
        self.model = []

        with open("model.json", "r") as f:
            json_file = json.load(f)

        for layer in json_file:
            weights = np.reshape(list(layer["weights"]), list(layer["weights_shape"]))
            bias = np.reshape(list(layer["bias"]), list(layer["bias_shape"]))

            activation_function = get_activation_function(layer["activation_function"])

            self.model.append(DenseLayer(layer["input_size"], layer["output_size"], activation_function, weights=weights, bias=bias))


    def architecture(self):
        """mostra a arquitetura da rede neural"""
        for i in range(len(self.model)):
            print(f"Layer: {i}")

            print(f"Neuronios de input: {self.model[i].input_size}")
            print(f"Neuronios de output: {self.model[i].output_size}")
            print(f"Função de ativação: {self.model[i].activation_function.name}")

            print()