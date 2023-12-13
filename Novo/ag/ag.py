import random

def mutate_weihts(gene):
    layer_sorteada = random.randint(0, len(gene) - 1)

    neuronio_a_mutar = random.randint(0, len(gene[layer_sorteada]["weights"]) - 1)
    peso_a_mutar = random.randint(0, len(gene[layer_sorteada]["weights"][neuronio_a_mutar]) - 1)

    gene[layer_sorteada]["weights"][neuronio_a_mutar][peso_a_mutar] = random.uniform(-1, 1)

    return gene

def mutate_bias(gene):
    layer_sorteada = random.randint(0, len(gene) - 1)

    neuronio_a_mutar = random.randint(0, len(gene[layer_sorteada]["bias"]) - 1)
    bias_a_mutar = random.randint(0, len(gene[layer_sorteada]["bias"][neuronio_a_mutar]) - 1)

    gene[layer_sorteada]["weights"][neuronio_a_mutar][bias_a_mutar] = random.uniform(-0.5, 0.5)

    return gene

class AG:
    def __init__(self) -> None:
        pass   
    
    def mutate(self, gene, qtd):
        for i in range(qtd):
            dice = random.randint(0, 1)

            if dice == 1:
                gene = mutate_weihts(gene)
            
            if dice == 0:
                gene = mutate_bias(gene)
        
        return gene