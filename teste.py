from rede_neural.rede_neural import Dense, Network

import numpy as np

model = Network([
    Dense(2, activation_function="Tanh", input_shape=(2, 1)),
    Dense(3, activation_function="Tanh"),
    Dense(1, activation_function="Tanh", input_shape=(1, 1))
])

x = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [[0], [1], [1], [0]]

print(model.predict(x[0]))