import numpy as np

#MSE = Mean Squared Error
class MSE():
    def __init__(self) -> None:
        pass

    def calcular(predizido, esperado):
        #calcula a função
        return np.mean(np.power(esperado - predizido), 2)
    
    def derivada(predizido, esperado):
        #calcula a derivada
        return 2 * (predizido - esperado) / np.size(esperado)