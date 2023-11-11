import random

from NeuralNetowrk.NeuralNetwork import NeuralNetwork

class AG:
    def __init__(self) -> None:
        pass

    def mutate_weihts(self, gene):
        number_of_layers = len(gene)
        layer_to_mutate = random.randint(0, number_of_layers - 2) #the last layer doesn't have weights 

        number_of_neurons = len(gene[layer_to_mutate])
        neuron_to_mutate = random.randint(0, number_of_neurons - 1)
        
        neuron_informations = gene[layer_to_mutate][neuron_to_mutate]

        number_of_links = len(neuron_informations) - 1 #minus 1 because the first element of that list it's the neuron itself
        link_to_mutate = random.randint(1, number_of_links)

        #so gene[layer_to_mutate][neuron_to_mutate][link_to_mutate][1] will have the weight that we want to mutate

        gene[layer_to_mutate][neuron_to_mutate][link_to_mutate][1] = random.uniform(-1, 1) #generate a hole new weight

        return gene #return the new gene
    
    def mutate_bias(self, gene):
        number_of_layers = len(gene)
        layer_to_mutate = random.randint(1, number_of_layers -1) #the first layer doesn't have bias (it is always 0)

        number_of_neurons = len(gene[layer_to_mutate])
        neuron_to_mutate = random.randint(0, number_of_neurons - 1)
        
        neuron_informations = gene[layer_to_mutate][neuron_to_mutate]

        number_of_links = len(neuron_informations) - 1 #minus 1 because the first element of that list it's the neuron itself
        link_to_mutate = random.randint(1, number_of_links)

        #so gene[layer_to_mutate][neuron_to_mutate][link_to_mutate][0] will have the bias that we want to mutate

        gene[layer_to_mutate][neuron_to_mutate][link_to_mutate][0] = random.uniform(-0.5, 0.5) #generate a hole new bias

        return gene #return the new gene    