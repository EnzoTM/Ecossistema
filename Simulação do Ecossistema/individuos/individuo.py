import random

def CriarIndividuo(gene, posicao, mapeamento, tipo):
        if gene[0] == None:
            for i in range(len(gene)):
                 gene[i] = random.randint(0, 4) #colcoar uma saída aleatório
        
        return Individuo(posicao=posicao, gene=gene, mapeamento=mapeamento, tipo=tipo) #criar o individuo

class Individuo:
    def __init__(self,posicao: list, gene: list, mapeamento: dict, tipo: int) -> None:
        self.posicao = posicao

        self.quantidade = 0

        self.gene = gene
        self.mapeamento = mapeamento

        self.tipo = tipo