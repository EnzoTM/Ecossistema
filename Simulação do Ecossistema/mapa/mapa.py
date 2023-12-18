import random
import math

"""
1: obstaculo
0: terra (pode andar em cima)
2: grama (comida da presa)
3: predador
4: presa
"""

"""
o ponto será da forma (y, x)
"""

def acao_y_x(p1, p2):
    """Calcula qual é a ação que se deve tomar para se aproximar mais rápidamente ao ponto p2 estando em p1"""
    acao_y = 0
    acao_x = 0

    if p1[0] < p2[0]:
        acao_y = 1
    elif p1[0] > p2[0]:
        acao_y = -1
    
    if p1[1] < p2[1]:
        acao_x = 1
    elif p1[1] > p2[1]:
        acao_x = -1

    return (acao_y, acao_x)

def calcula_distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class Mapa:
    def __init__(self, x, y, obstaculo_chance = 0.25, terra_chance=0.5, grama_chance=0.25) -> None:
        self.mapa: list[list] = []

        self.grass_regenerating = []
        self.presas_mortas = []

        self.x: int  = x
        self.y: int = y

        for i in range(y):
            self.mapa.append([-1])
            if i == 0 or i == y-1:
                for k in range(x):
                    self.mapa[i].append(-1)

            for j in range(1, x-1):
                valor_a_ser_adicionado = random.choices([0, 1, 2], weights=[terra_chance, obstaculo_chance, grama_chance])[0]
                self.mapa[i].append(valor_a_ser_adicionado)

            self.mapa[i].append(-1)

    def __getitem__(self, position):
        return self.mapa[position[0]][position[1]]

    def printar_mapa(self)->None:   
        for y in range(self.y):
            for x in range(self.x):
                valor = self.mapa[y][x]

                if self.mapa[y][x] < 0 and (y == 0 or y == self.y-1):
                    if valor == 4:
                        print("\033[91m" + str(valor) + "\033[0m", end="")
                    elif valor == 3:
                        print("\033[94m" + str(valor) + "\033[0m", end="")
                    elif valor == 2:
                        print("\033[92m" + str(valor) + "\033[0m", end="")
                    elif valor == -1:
                        print("\033[90m" + str(valor) + "\033[0m", end="")
                    else:
                        print(str(valor), end="")
                else:
                    if valor == 4:
                        print("\033[91m" + str(valor) + "\033[0m", end=" ")
                    elif valor == 3:
                        print("\033[94m" + str(valor) + "\033[0m", end=" ")
                    elif valor == 2:
                        print("\033[92m" + str(valor) + "\033[0m", end=" ")
                    elif valor == -1:
                        print("\033[90m" + str(valor) + "\033[0m", end=" ")
                    else:
                        print(str(valor), end=" ")

            print()

    def surroundings(self, posicao, alcance, tipo):
        """
        TODO
        dada uma posição do mapa (y, x)
        retornar uma matriz de todos os blocos do mapa a "alcance" de distancia
        tem que conter o ponto (y, x)
        """
        tem_comida = 0
        posicao_comida = (-1, -1)

        tem_aliado = 0
        posicao_aliado = (-1, -1)

        tem_inimigo = 0
        posicao_inimigo = (-1, -1)

        surroundings = []

        contador = -1

        comida = tipo - 1
        aliado = tipo
        
        if tipo == 3:
            inimigo = 4
        else:
            inimigo = -2 #nao existe

        #para todos os y's
        for i in range(posicao[0] - alcance, posicao[0] + alcance + 1): #posicao[1] é y
            surroundings.append([])

            contador += 1

            #para todos os x's
            for j in range(posicao[1] - alcance, posicao[1] + alcance + 1):
                if (i < 0 or i >= self.x) or (j < 0 or j >= self.y):
                    surroundings[contador].append(-1)
                else:
                    if (self.mapa[i][j] == comida): #se tiver comida
                        if tem_comida == 0:
                            tem_comida = 1

                            posicao_comida = (i, j)
                        else:
                            distancia = calcula_distancia(posicao, (i, j)) #calcular a distancia dessa comida

                            if distancia < calcula_distancia(posicao, posicao_comida): #se essa distancia for menor do que a anterior
                                posicao_comida = (i, j)

                    elif (self.mapa[i][j] == aliado) and ((i, j) != posicao):
                        if tem_aliado == 0:
                            tem_aliado = 1

                            posicao_aliado = (i, j)
                        else:
                            distancia = calcula_distancia(posicao, (i, j)) #calcular a distancia desse aliado

                            if distancia < calcula_distancia(posicao, posicao_aliado): #se essa distancia for menor do que a anterior
                                posicao_aliado = (i, j)


                    elif self.mapa[i][j] == inimigo:
                        if tem_inimigo == 0:
                            tem_inimigo = 1

                            posicao_inimigo = (i, j)
                        else:
                            distancia = calcula_distancia(posicao, (i, j))

                            if distancia < calcula_distancia(posicao, posicao_inimigo):
                                posicao_inimigo = (i, j)

                    surroundings[contador].append(self.mapa[i][j])
        
        return surroundings, tem_comida, posicao_comida, tem_aliado, posicao_aliado, tem_inimigo, posicao_inimigo

    
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
    
    def move(self, posicao_atual:tuple ,anda_y:int, anda_x:int, comida: int):
        conteudo_novo_local = self.mapa[posicao_atual[0] + anda_y][posicao_atual[1] + anda_x]

        if  (conteudo_novo_local != 0) and (conteudo_novo_local != comida): #está tentando fazer uma ação inválida
            return posicao_atual , 0.1 #retorno de ação inválida

        #se chegou aqui singifca que a ação pode ser feita

        indv:int  = self.mapa[posicao_atual[0]][posicao_atual[1]] #pega o tipo de indv que estava na local

        self.mapa[posicao_atual[0]][posicao_atual[1]] = 0 #local atual fica disponivel

        valor_nova_posicao = self.mapa[posicao_atual[0] + anda_y][posicao_atual[1] + anda_x] #pegar o valor que tinha na posição

        self.mapa[posicao_atual[0] + anda_y][posicao_atual[1] + anda_x] = indv #colocar o indivíduo na nova posição
        
        if (valor_nova_posicao == comida): #chegou em uma comida
            if valor_nova_posicao == 3: #se for uma presa
                self.presas_mortas.append((posicao_atual[0] + anda_y, posicao_atual[1] + anda_x)) #adicionar esta posição a posicao de presas que morreram

            return ((posicao_atual[0] + anda_y) , (posicao_atual[1] + anda_x)), -0.2 #boa ação, pois comeu
 
        return ((posicao_atual[0] + anda_y) , (posicao_atual[1] + anda_x)) , 0.0 #ação que nao foi boa nem ruim
    
    def make_action(self, action, individuo_tipo, postion, tem_comida, comida, tem_aliado, aliado, tem_inimigo = False, inimigo = None):
        if action == 0: #ir para a comida mais proxima
            if tem_comida == False:
                return (postion, 0.1) #ação invalida

            acao_y, acao_x = acao_y_x(postion, comida) #calcular a ação que deve ser feita

            return self.move(postion, acao_y, acao_x, comida=individuo_tipo - 1)
        
        if action == 1: #ir para o aliado mais proximo
            if tem_aliado == False:
                return (postion, 0.1) #ação invalida

            acao_y, acao_x = acao_y_x(postion, aliado)

            return self.move(postion, acao_y, acao_x,comida=individuo_tipo - 1)
        
        if action == 2: #ir ao lado contrario do inimigo mais proximo
            if tem_inimigo == False:
                return (postion, 0.1) #ação inválida
            
            acao_y, acao_x = acao_y_x(postion, inimigo) #calcular a ação que deve ser feita

            return self.move(postion, -acao_y, -acao_x, comida=individuo_tipo - 1)

        if action == 3: #ficar parado
            return postion, 0 
        
        if action == 4: #andar aleatoriamente
            return self.move(postion, random.randint(-1, 1), random.randint(-1, 1), comida=individuo_tipo - 1)
        
    def mudar_valor(self, posicao: tuple, valor: int):
        """muda o valor de um local do mapa"""
        self.mapa[posicao[0]][posicao[1]] = valor