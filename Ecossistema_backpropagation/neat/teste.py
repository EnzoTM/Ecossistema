from NeuralNetwork.NeuralNetwork import NeuralNetwork, Dense

from ag.ag import AG

import json

ag = AG()

model = [
    Dense(4, activation_function="Tanh", input_shape=(4,)),
    Dense(2, activation_function="Tanh", input_shape=(2,))
]

individuo = NeuralNetwork()
individuo.CreateNetwrok(model_strucutre=model)

print(individuo.predict([1, -1, 0.1, 2]))

individuo.TrainDuringSimulation((1, 1), (0, 0))