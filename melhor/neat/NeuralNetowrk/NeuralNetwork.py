import random

class Neuron:
    def __init__(self, id: int, links: list, bias: int = None):
        #set the bias value
        if bias == None:
            self.bias = random.uniform(-0.5, 0.5)
        else:
            self.bias = bias

        self.id = id

        self.value = 0

        self.links = links #neurons to witch this neuron is linked to 


class Link:
    def __init__(self, neuron: Neuron, weight: float= None):
        #set the weight value
        if weight == None:
            self.weight = random.uniform(-1, 1)
        else:
            self.weight = weight

        self.neuron = neuron


class NeuralNetwork:
    def __init__(self):
        self.layers = []

        self.number_of_neurons = 0
        
    def add_neuron(self, layer: int, links: list, bias: int = None, id: int = None):
        if len(self.layers) == layer: #if this layer don't yet exist
            self.layers.append([]) #create a new layer

        if id == None: id = self.number_of_neurons #if no id is given, then the id will be the number of nuerons

        self.layers[layer].append(Neuron(id = id, links=links, bias=bias)) #create the new neuron
        self.number_of_neurons += 1
    
    def add_link(self, neuron_id, links: list):
        neuron = self.search_neuron(neuron_id) #search for the neuron

        if neuron == None: return False #if the neuron was not found

        for link in links:
            neuron.links.append(link) #append all the links

        return True
    
    def NeuralNetworkPrint(self):
        for layer in range(len(self.layers)): #for each layer on the neural network
            print(f"Layer: {layer}")

            for i in range(len(self.layers[layer])): #for each neuron on that layer
                neuron = self.layers[layer][i] 

                print(f"Neuron: {neuron.id}. Links:", end=" ")

                for link in neuron.links: #for each link that this neuron has
                    print(f"{link.neuron.id} ({link.weight})", end=" ")
                
                print()

            print(end="\n")    

    def search_neuron(self, id: int):
        for layer in range(len(self.layers)): #for each layer
            for neuron in range(len(self.layers[layer])): #for each neuron on the layer
                if id == self.layers[layer][neuron].id: #if it is the neuron that we are looking for
                    return self.layers[layer][neuron] #return the neuron
                
        return None #implies that the neuron was not on the neural_network
    
    def predict(self, inputs: list):
        #verify if the right input shape was given
        if len(inputs) != len(self.layers[0]):
            print(f"Invalid input shape. Given: {len(inputs)}. Expected: {len(self.layers[0])}")

            return None

        #logic for the input layer
        for i in range(len(self.layers[0])): #for every neuron on the input layer
            self.layers[0][i].value = inputs[i] + self.layers[0][i].bias #set the value of the neruon based on the input and it's bias

            neuron = self.layers[0][i] #get the neuron

            for link in neuron.links:#for each link that this neuron has
                link.neuron.value += (neuron.value * link.weight) #calculate the weighted value for the neuron that it is linked to
        
        #logic for all the hidden layers
        for i in range(1, len(self.layers) - 1): #for all the hidden layers
            layer = self.layers[i] #get the current layer

            #for each neuron in the layer
            for neuron in layer:
                neuron.value += neuron.bias #add the bias for the current neuron

                for link in neuron.links:
                    link.neuron.value += (neuron.value * link.weight) #add the weighted value to the next neuron

                neuron.value = 0 #reset the value of this neuron for the next prediction

        #logic for the output layer
        layer = self.layers[-1]

        output = [] #output list that will be returned

        #for each neuron on the output layer
        for neuron in layer: 
            neuron.value += neuron.bias #add the bias to it's value
            
            output.append(neuron.value) #append the result on the output list

            neuron.value = 0 #reset the value of this neuron for the next prediction

        return output #return the results
    
    def GetGene(self):
        gene = []

        for layer in range(len(self.layers)): #for each layer on the neural network
            gene.append([]) #create the layer

            for i in range(len(self.layers[layer])): #for each neuron on that layer
                gene[layer].append([]) #create the neuron

                neuron = self.layers[layer][i] 

                gene[layer][i].append([neuron.id, neuron.bias]) #append the information about the neuron

                for link in neuron.links: #for each link that this neuron has
                    gene[layer][i].append([link.neuron.id, link.weight])
        
        return gene
    
    def CreateNetwrok(self, gene: list):
        self.network_id = []

        #for each layer of the gene
        for i in range(len(gene)):
            layer = gene[i]

            self.layers.append([]) #create the layer
            
            #to create the links it's necessary that all the neurons already exist, so, this part of the code will only create the neurons
            for neuron in layer:
                neuron_informations = neuron[0] #get the informations about the neuron it self

                #create the new neron
                self.add_neuron(layer=i, links=[], bias=neuron_informations[1], id = neuron_informations[0])

        #right now all the neurons had been created, so we just need to create the links

        #for each layer
        for i in range(len(gene)):
            self.network_id.append([]) #adicionar a lista referente aquela layer

            for j in range(len(gene[i])): #for each neuron     
                neuron = self.layers[i][j] #get the neuron

                neuron_informations = gene[i][j]

                self.network_id[i].append(len(neuron_informations) - 1) #minus 1, cause we just want to know how many links this neuron has

                for k in range(1, len(neuron_informations)): #for all it's links
                    link = Link(self.search_neuron(neuron_informations[k][0]), weight=neuron_informations[k][1])

                    neuron.links.append(link)