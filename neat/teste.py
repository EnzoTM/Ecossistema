from ag import AG
from NeuralNetowrk.NeuralNetwork import NeuralNetwork

gene = [
    [[[0, 0], [2, 0.3]], [[1, 0], [2, 0.2]]],
    [[[2, 0], [3, 2]]],
    [[[3, 0]]]
]

ag = AG()

nn = NeuralNetwork()
nn.CreateNetwrok(gene)

nn.NeuralNetworkPrint()

nn2 = NeuralNetwork()
nn2.CreateNetwrok(ag.mutate(gene))

nn2.NeuralNetworkPrint()