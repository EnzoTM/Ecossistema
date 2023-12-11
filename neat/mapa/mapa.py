import random
import math

from individuos.individuo import Individuo

"""
1: obstaculo
0: terra (pode andar em cima)
2: grama
3: predador
4: presa
"""

"""
o ponto será da forma (y, x)
"""

def calcula_distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calcula_input(valor: int, distancia: float):
        if (valor == 2): #é uma grama
            return 1 / distancia
        
        if (valor == 3): #aliado
            return -1 / distancia

class Mapa:
    def __init__(self, x, y, obstaculo_chance = 0.25, terra_chance=0.5, grama_chance=0.25) -> None:
        self.mapa: list[list] = []

        self.positions_withgrass:list = []

        self.x: int  = x
        self.y: int = y

        for i in range(y):
            self.mapa.append([-1])

            if i == 0 or i == y-1:
                for k in range(x):
                    self.mapa[i].append(-1)

            for _ in range(1, x-1):
                self.mapa[i].append(random.choices([0, 1, 2], weights=[terra_chance, obstaculo_chance, grama_chance])[0])

                if self.mapa[i] == 2: #se for uma grama, adicionar a posição na lista de posições que tem grama
                    self.positions_with_grass.append([y, x])

            self.mapa[i].append(-1)

    def atualizar(self, individuos: list[Individuo]):
         #atualizar o mapa
        for individuo in individuos:
            posicao = individuo.posicao #na posicao de cada indivíduo
            
            #ou colocar uma terra ou uma grama no local de onde estava o indivíduo
            self.mapa[posicao[0]][posicao[1]] = random.choices([0, 2], weights=[0.75, 0.25])[0]

    def printar_mapa(self)->None:   
        for y in range(self.y):
            for x in range(self.x):
                if self.mapa[y][x] < 0 and (y == 0 or y == self.y-1):
                    print(self.mapa[y][x], end="")
                else:
                    print(self.mapa[y][x], end=" ")

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

        #para todos os y's
        for i in range(posicao[1] - alcance, posicao[1] + alcance + 1): #posicao[1] é y
            surroundings.append([])

            contador += 1

            #para todos os x's
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

            if self.mapa[y][x] == 0:
                self.mapa[y][x] = tipo

                return (y, x)
    
    def move(self, posicao_atual:tuple ,anda_y:int, anda_x:int):

        conteudo_novo_local = self.mapa[posicao_atual[0] + anda_y][posicao_atual[1] + anda_x]

        if  (conteudo_novo_local != 0) and (conteudo_novo_local != 2): #posicao atual somada a somas na posicao y e x é -1 (borda)
            return posicao_atual , 0.1 #nao anda e ganha fome

        #se chegou aqui singifca que a ação pode ser feita

        indv:int  = self.mapa[posicao_atual[0]][posicao_atual[1]] #pega o tipo de indv que estava na loca

        self.mapa[posicao_atual[0]][posicao_atual[1]] = 0 #local atual fica disponivel

        self.mapa[posicao_atual[0] + anda_y][posicao_atual[1] + anda_x] = indv

        if ( ((posicao_atual[0] + anda_y) , (posicao_atual[1] + anda_x)) in self.positions_withgrass  ): # se ele for para grama, come a grama e perde fome
            self.positions_withgrass.remove(((posicao_atual[0] + anda_y) , (posicao_atual[1] + anda_x)))  #remove posicao da lista de gramas

            return ((posicao_atual[0] + anda_y) , (posicao_atual[1] + anda_x)) , -0.3
 
        return ((posicao_atual[0] + anda_y) , (posicao_atual[1] + anda_x)) , 0.0
    
    def make_action(self, action, postion):
        if action == 0: return postion, 0 #nao vai mudar a fome
        
        if action == 1: return self.move(postion, -1, 0) #ir pra cima

        if action == 2: return self.move(postion, 1, 0) #ir pra baixo

        if action == 3: return self.move(postion, 0, 1) #ir pra direita

        if action == 4: return self.move(postion, 0, -1) #ir pra esquerda

    def inputs(self, position):
        inputs_ = []

        y = position[0]
        x = position[1]

        flag = 1
        for i in range(y - 1, -1): #for(int i = y - 1; i >= 0; i--)
            if (self.mapa[i][x] != 0) and (self.mapa[i][x] != -1):
                flag = 0
                inputs_.append(calcula_input(self.mapa[i][x], calcula_distancia((i, x), (y, x))))

                break
        if flag: inputs_.append(0)

        flag = 1
        for i in range(y + 1, self.y):
            if (self.mapa[i][x] != 0) and (self.mapa[i][x] != -1):
                flag = 0
                inputs_.append(calcula_input(self.mapa[i][x], calcula_distancia((i, x), (y, x))))

                break
        if flag: inputs_.append(0)

        flag = 1
        for i in range(x - 1, -1, -1):
            if (self.mapa[y][i] != 0) and (self.mapa[y][i] != -1):
                flag = 0
                inputs_.append(calcula_input(self.mapa[y][i], calcula_distancia((y, i), (y, x))))

                break
        if flag: inputs_.append(0)

        flag = 1
        for i in range(x + 1, self.x):
            if (self.mapa[y][i] != 0) and (self.mapa[y][i] != -1):
                flag = 0
                inputs_.append(calcula_input(self.mapa[y][i], calcula_distancia((y, i), (y, x))))
                
                break
        if flag: inputs_.append(0)

        return inputs_