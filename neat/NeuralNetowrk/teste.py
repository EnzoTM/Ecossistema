from NeuralNetwork import NeuralNetwork, Link

model1 = NeuralNetwork()

#input layer
for i in range(2):
    model1.add_neuron(0, [], bias=0)

#single neuron hidden layer
model1.add_neuron(1, [], bias=0)

#output layer
model1.add_neuron(2, [], bias=0)

model1.add_link(0, [Link(model1.search_neuron(2), 0.3)])
model1.add_link(1, [Link(model1.search_neuron(2), 0.2)])
model1.add_link(2, [Link(model1.search_neuron(3), 2)])  

print(model1.predict([1, 2]))

gene = [
    [[[0, 0], [2, 0.3]], [[1, 0], [2, 0.2]]],
    [[[2, 0], [3, 2]]],
    [[[3, 0]]]
]

model2 = NeuralNetwork()

model2.CreateNetwrok(gene)

print(model2.predict([1, 2]))