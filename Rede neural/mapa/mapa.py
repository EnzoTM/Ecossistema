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

        self.positions_withgrass:set = set()

        self.x: int  = x
        self.y: int = y

        #cria o mapa
        for i in range(y):
            self.mapa.append([-1])
            if i == 0 or i == y-1:
                for k in range(x):
                    self.mapa[i].append(-1)

            for j in range(1, x-1):
                valor_a_ser_adicionado = random.choices([0, 1, 2], weights=[terra_chance, obstaculo_chance, grama_chance])[0]
                self.mapa[i].append(valor_a_ser_adicionado)

                if valor_a_ser_adicionado == 2: #se for uma grama, adicionar a posição na lista de posições que tem grama
                    self.positions_withgrass.add((i, j))

            self.mapa[i].append(-1)


    def printar_mapa(self)->None: 
        """priinta o mapa na tela"""  
        for y in range(self.y):
            for x in range(self.x):
                valor = self.mapa[y][x]

                if self.mapa[y][x] < 0 and (y == 0 or y == self.y-1):
                    if valor == 3:
                        print("\033[91m" + str(valor) + "\033[0m", end="")
                    elif valor == 2:
                        print("\033[92m" + str(valor) + "\033[0m", end="")
                    elif valor == -1:
                        print("\033[90m" + str(valor) + "\033[0m", end="")
                    else:
                        print(str(valor), end="")
                else:
                    if valor == 3:
                        print("\033[91m" + str(valor) + "\033[0m", end=" ")
                    elif valor == 2:
                        print("\033[92m" + str(valor) + "\033[0m", end=" ")
                    elif valor == -1:
                        print("\033[90m" + str(valor) + "\033[0m", end=" ")
                    else:
                        print(str(valor), end=" ")

            print()
    
    def posicao_disponivel(self, tipo):
        #retorna uma posição disponível onde o indivíduo do tipo (tipo) foi inserido
        while(True):
            x = random.randint(0, self.x - 1)
            y = random.randint(0, self.y - 1)

            if self.mapa[y][x] == 0:
                self.mapa[y][x] = tipo

                return (y, x)
    
    def move(self, posicao_atual:tuple ,anda_y:int, anda_x:int):
        conteudo_novo_local = self.mapa[posicao_atual[0] + anda_y][posicao_atual[1] + anda_x]

        if  (conteudo_novo_local != 0) and (conteudo_novo_local != 2): #local indisponível
            return posicao_atual , 0.1 #ação inválida

        #se chegou aqui singifca que a ação pode ser feita

        indv:int  = self.mapa[posicao_atual[0]][posicao_atual[1]] #pega o tipo de indv que estava na loca
 
        self.mapa[posicao_atual[0]][posicao_atual[1]] = 0 #local atual fica disponivel

        self.mapa[posicao_atual[0] + anda_y][posicao_atual[1] + anda_x] = indv #o novo local passa a ser o indivíduo
        
        if ( (posicao_atual[0] + anda_y , posicao_atual[1] + anda_x) in self.positions_withgrass): # se ele for para grama, come a grama e perde fome
            self.positions_withgrass.remove(((posicao_atual[0] + anda_y) , (posicao_atual[1] + anda_x)))  #remove posicao da lista de gramas

            return ((posicao_atual[0] + anda_y) , (posicao_atual[1] + anda_x)), -1 #ação boa, pois comeu
 
        return ((posicao_atual[0] + anda_y) , (posicao_atual[1] + anda_x)) , 0.0 #ação nem boa nem ruim
    
    def make_action(self, action, postion):
        if action == 0: return postion, 0 #ficar parado (retorna zero, pois é uma ação nem boa nem ruim)
        
        if action == 1: return self.move(postion, -1, 0) #ir pra cima

        if action == 2: return self.move(postion, 1, 0) #ir pra baixo

        if action == 3: return self.move(postion, 0, 1) #ir pra direita

        if action == 4: return self.move(postion, 0, -1) #ir pra esquerda

    def inputs(self, position):
        """
        input funciona da forma:
        se não achou nada retorna 0
        se achou uma comida retorna 1 / distancia
        se achou um aliado retorna -1 / distancia
        """
        inputs_ = []

        y = position[0]
        x = position[1]

        #pega qual será o input em cima do indivíduo
        flag = 1
        for i in range(y - 1, -1): #for(int i = y - 1; i >= 0; i--)
            if (self.mapa[i][x] != 0) and (self.mapa[i][x] != -1): #se for comida ou aliado
                flag = 0
                inputs_.append(calcula_input(self.mapa[i][x], calcula_distancia((i, x), (y, x))))

                break
        if flag: inputs_.append(0)

        #pega qual será o input em baixo do indivíduo
        flag = 1
        for i in range(y + 1, self.y):
            if (self.mapa[i][x] != 0) and (self.mapa[i][x] != -1): #se for comida ou aliado
                flag = 0
                inputs_.append(calcula_input(self.mapa[i][x], calcula_distancia((i, x), (y, x))))

                break
        if flag: inputs_.append(random.randint(-1, 1))

        #pega qual será o input a esquerda do indivíduo
        flag = 1
        for i in range(x - 1, -1, -1):
            if (self.mapa[y][i] != 0) and (self.mapa[y][i] != -1): #se for comida ou aliado
                flag = 0
                inputs_.append(calcula_input(self.mapa[y][i], calcula_distancia((y, i), (y, x))))

                break
        if flag: inputs_.append(0)

        #pega qual será o input a direita do indivíduo
        flag = 1
        for i in range(x + 1, self.x):
            if (self.mapa[y][i] != 0) and (self.mapa[y][i] != -1): #se for comida ou aliado
                flag = 0
                inputs_.append(calcula_input(self.mapa[y][i], calcula_distancia((y, i), (y, x))))
                
                break
        if flag: inputs_.append(0)

        return inputs_
    
    def mudar_valor(self, posicao: tuple, valor: int):
        self.mapa[posicao[0]][posicao[1]] = valor