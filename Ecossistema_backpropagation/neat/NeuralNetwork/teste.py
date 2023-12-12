from NeuralNetwork import NeuralNetwork, Dense

model = [
    Dense(2, activation_function="Tanh", input_shape=(4, 2, 1)),
    Dense(3, activation_function="Tanh"),
    Dense(1, activation_function="Tanh", input_shape=(4, 1, 1))
]


network = NeuralNetwork()
network.create_model(model_strucutre=model)

network.architecture()

gene = network.GetGene()

layer = len(gene)