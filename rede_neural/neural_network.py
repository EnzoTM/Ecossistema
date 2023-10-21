from classes import Dense, Activation
from loss import MSE
from activation_functions import Tanh

def predict(network, input):
    prediction = input

    #"andar" nas camadas da rede neural para calcular o resultado
    for layer in network:
        prediction = layer.forward(prediction)

    return prediction

def train(network, loss, x_train, y_train, epochs = 1000, learning_rate = 0.01, verbose = True):
    for epoch in range(0, epochs): #para cada epoch
        for x, y in zip(x_train, y_train): #para cada par (x, y)
            prediction = predict(network, x) #pegar a predicao da rede neural

            erro = loss.calcular(y, prediction) #calcular a loss dela

            gradiente = loss.derivada(y, prediction) #calcular o gradietne

            #"andar" na rede neural ao contrário para fazer o algorítmo de backpropagation
            for layer in reversed(network):
                gradiente = layer.backward(gradiente, learning_rate)

        
        erro = erro / len(x_train)

        if verbose:
            print(f"Epoch: {epoch} --> Loss: {erro}")