import random

"""
1: obstaculo
0: terra (pode andar em cima)
2: grama
3: predador
4: presa
"""

class Mapa:
    def __init__(self, x, y, obstaculo_chance = 0.25, terra_chance=0.5, grama_chance=0.25) -> None:
        self.mapa = []

        self.x = x
        self.y = y

        for i in range(x):
            self.mapa.append([])

            for _ in range(y):
                self.mapa[i].append(random.choices([0, 1, 2], weights=[terra_chance, obstaculo_chance, grama_chance])[0])

    def atualizar(self, new_tree_probability):
        for i in range(0, self.x * self.y):
            new_tree = random.choices([0, 1], weights=[1 - new_tree_probability, new_tree_probability])[0]

            if new_tree:
                x = random.randint(0, 1)
                y = random.randint(0, 1)

                if self.mapa[x][y] == 0:
                    self.mapa[x][y] = 2

    def printar_mapa(self):
        for x in range(self.x):
            for y in range(self.y):
                print(self.mapa[x][y], end=" ")
            
            print()

    def surroundings(self, posicao, alcance):
        """
        TODO
        dada uma posição do mapa (x, y)
        retornar uma matriz de todos os blocos do mapa a "alcance" de distancia
        tem que conter o ponto (x, y)
        """
        surroundings = []

        contador = -1

        for i in range(posicao[1] - alcance, posicao[1] + alcance + 1):
            surroundings.append([])

            contador += 1

            for j in range(posicao[0] - alcance, posicao[0] + alcance + 1):
                if (i < 0 or i >= self.x) or (j < 0 or j >= self.y):
                    surroundings[contador].append(1)
                else:
                    surroundings[contador].append(self.mapa[i][j])
        
        return surroundings
    
    def posicao_disponivel(self, tipo):
        #esse tipo é o que será armazenado na nova posição
        #um predador ou uma presa

        #tratar o fato de que o mapa pode estar cheio
        while(True):
            x = random.randint(0, self.x - 1)
            y = random.randint(0, self.y - 1)

            if self.mapa[x][y] == 0:
                self.mapa[x][y] = tipo

                return (x, y)