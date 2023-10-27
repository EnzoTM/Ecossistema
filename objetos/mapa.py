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

        self.positions_with_grass = []

        self.x = x
        self.y = y

        for i in range(x):
            self.mapa.append([])

            for _ in range(y):
                self.mapa[i].append(random.choices([0, 1, 2], weights=[terra_chance, obstaculo_chance, grama_chance])[0])

                if self.mapa[i] == 2: #se for uma grama, adicionar a posição na lista de posições que tem grama
                    self.positions_with_grass.append([x, y])

    def atualizar(self, new_grass_probability):
        for i in range(0, self.x * self.y):
            new_grass = random.choices([0, 1], weights=[1 - new_grass_probability, new_grass_probability])[0]

            if new_grass:
                x = random.randint(0, 1)
                y = random.randint(0, 1)

                if self.mapa[x][y] == 0:
                    self.mapa[x][y] = 2
                    self.positions_with_grass.append([x, y])

    def printar_mapa(self):
        for x in range(self.x):
            for y in range(self.y):
                print(self.mapa[x][y], end=" ")
            
            print()

    def surroundings(self, posicao, alcance):
        """
        TODO
        dada uma posição do mapa (y, x)
        retornar uma matriz de todos os blocos do mapa a "alcance" de distancia
        tem que conter o ponto (y, x)
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
    
    def move_up(self, position):
        """nao precisa ser uma função da classe, mas usa variaveis dela ent coloquei aqui para simplificar"""
        #nao pode subir
        if (position[0] == 0): return -1 #vai perder 1 de vida, por isso retorna -1
        
        if (position[0] - 1 != 0) and (position[0] - 1 != 2): return -1

        #se chegou aqui singifca que a ação pode ser feita

        tmp = self.mapa[position[0], position[1]]

        if position in self.positions_with_grass:
            self.mapa[position[0], position[1]] = 2

            self.positions_with_grass.remove(position)
        else:
            self.mapa[position[0], position[1]] = 0

        self.mapa[position[0] - 1, position[1]] = tmp

        return 0
    
    def move_down(self, position):
        """nao precisa ser uma função da classe, mas usa variaveis dela ent coloquei aqui para simplificar"""
        #nao pode descer
        if (position[0] == (self.y - 1)): return -1 #vai perder 1 de vida, por isso retorna -1
        
        if (position[0] - 1 != 0) and (position[0] - 1 != 2): return -1

        #se chegou aqui singifca que a ação pode ser feita

        tmp = self.mapa[position[0], position[1]]

        if position in self.positions_with_grass:
            self.mapa[position[0], position[1]] = 2

            self.positions_with_grass.remove(position)
        else:
            self.mapa[position[0], position[1]] = 0

        self.mapa[position[0] + 1, position[1]] = tmp

        return 0

    
    def make_action(self, action, postion):
        if action == 0: return 0 #nao vai perder nada de vida
        
        if action == 1:  return self.move_up(postion)