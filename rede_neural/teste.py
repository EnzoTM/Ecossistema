from rede_neural import Network, Dense

model = Network([
    Dense(2, activation_function="Tanh", input_shape=(4, 2, 1)),
    Dense(3, activation_function="Tanh"),
    Dense(5, activation_function="Tanh"),
    Dense(1, activation_function="Tanh", input_shape=(4, 1, 1))
])

#model.architecture()

x = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [[0], [1], [1], [0]]

#model.train(x, y, 0.1, "MSE", 1000)

#model.save()

model.open_model()

model.architecture()