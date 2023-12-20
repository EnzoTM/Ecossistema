import pygame
from mapa.mapa import Mapa
from individuos.individuo import CriarIndividuo
from copy import copy

import time


# 1: obstaculo
# 0: terra (pode andar em cima)
# 2: grama (comida)
# 4: predador
# 3: presa

def atualizar_tela(self, screen, escala_x, escala_y):
        for y in range(self.y):
            for x in range(self.x):
                posicao = (y, x)
                tipo_terreno = self.mapa.__getitem__(position=posicao)

class Imagem():
    def __init__(self, x_mapa: int, y_mapa: int, mapa: Mapa, geracao: int):
        self.x = x_mapa
        self.y = y_mapa
        self.mapa = mapa
        self.geracao = geracao

    def imagem(self):
        pygame.init()
        # Configurações da tela
        screen_width = 900
        screen_height = 700
        screen = pygame.display.set_mode((screen_width, screen_height))
        
        pygame.display.set_caption(f'Geração: {self.geracao}')
        
        # Carregar imagens
        grama_image = pygame.image.load('img/floor.png')
        grama_image = pygame.transform.scale(grama_image, (int(screen_width / self.x), int(screen_height / self.y)))

        earth_image = pygame.image.load('img/earth.png')
        earth_image = pygame.transform.scale(earth_image, (int(screen_width / self.x), int(screen_height / self.y)))

        rock_image = pygame.image.load('img/rock.png')
        rock_image = pygame.transform.scale(rock_image, (int(screen_width / self.x), int(screen_height / self.y)))
        
        presa = pygame.image.load('img/presa.png')
        presa = pygame.transform.scale(presa, (int(screen_width / self.x), int(screen_height / self.y)))
        
        predador = pygame.image.load('img/predador.png')
        predador = pygame.transform.scale(predador, (int(screen_width / self.x), int(screen_height / self.y)))

        while(True):
            for i in range(tamanho):
                # comando = input()

                # if comando == '1': break #reinicia tudo

                tmp = copy(mapa.presas_mortas) #cópia da lista de presas mortas

                for h in range(len(tmp)): #para cada presa morta
                    posicao = mapa.posicao_disponivel(3) #pegar uma novoa posição para a presa spawnar

                    for j in range(len(presas)):
                        if presas[j].posicao == tmp[h]: #achar qual q é a presa q morreu
                            presas[j].posicao = posicao #atualizar sua posição

                            presas[j].quantidade = 0 #zerar a pontuação dela, pois ela morreu

                            mapa.presas_mortas.remove(tmp[h]) #remover da lista de presas mortas

                if i < len(presas): #essa presa existe
                    retorno = mapa.surroundings(presas[i].posicao, 3, tipo=3) #pegar os inputs da presa
                            
                    inputs = str(retorno[1]) + str(retorno[3]) + str(retorno[5]) #transformar no input necessário para fazer uma ação
                    acao = presas[i].gene[mapeamento_presa[inputs]] #pegar a ação

                    #fazer a ação
                    nova_posicao, resultado = mapa.make_action(action=acao, postion=presas[i].posicao, tem_comida=retorno[1], comida=retorno[2], tem_aliado=retorno[3], aliado=retorno[4], tem_inimigo=retorno[5], inimigo=retorno[6], individuo_tipo=3)
                    presas[i].posicao = nova_posicao #atualizar a posição do indivíduo
            
                if i < len(predadores): #nao existe esse predador
                    retorno = mapa.surroundings(predadores[i].posicao, 3, tipo=4) #pegar os inputs do predador

                    inputs = str(retorno[1]) + str(retorno[3]) #transformar no input necessário para fazer uma ação
                    acao = predadores[i].gene[mapeamento_predador[inputs]] #pegar a ação

                    #fazer a ação
                    nova_posicao, resultado = mapa.make_action(action=acao, postion=predadores[i].posicao, tem_comida=retorno[1], comida=retorno[2], tem_aliado=retorno[3], aliado=retorno[4], individuo_tipo=4)
                    predadores[i].posicao = nova_posicao #atualizar a posição do indivíduo
                
                time.sleep(0.2)

                escala_x = screen_width / self.x
                escala_y = screen_height / self.y

                for y in range(self.y):
                    for x in range(self.x):
                        posicao = (y,x)
                        tipo_terreno = self.mapa.__getitem__(position=posicao)
                        if tipo_terreno == 1:  # Obstáculo 
                            screen.blit(rock_image, (x * escala_x, y * escala_y))
                        elif tipo_terreno == 0:  # Espaço livre - terra
                            screen.blit(earth_image, (x * escala_x, y * escala_y))
                        elif tipo_terreno == 2:  # Grama
                            screen.blit(grama_image, (x * escala_x, y * escala_y))
                        elif tipo_terreno == 4:  # Predador
                            screen.blit(predador, (x * escala_x, y * escala_y))
                        elif tipo_terreno == 3:  # Presa
                            screen.blit(presa, (x * escala_x, y * escala_y))
                #self.atualizar_tela(screen, escala_x, escala_y)

                pygame.display.flip()  # Atualiza a tela


mapeamento_presa = {
    "000": 0,
    "001": 1,
    "010": 2,
    "011": 3,
    "100": 4,
    "101": 5,
    "110": 6,
    "111": 7
}
mapeamento_predador = {
    "00": 0,
    "01": 1,
    "10": 2,
    "11": 3
}

gene_predador = [3, 4, 4, 0]
gene_presa = [1, 0, 2, 2, 0, 0, 0, 0]

numero_de_presas = 20
numero_de_predadores = 10

geracao = 0 

if numero_de_predadores > numero_de_presas: tamanho = numero_de_predadores
else: tamanho = numero_de_presas

while(True):
    mapa = Mapa(20, 20, obstaculo_chance=0, terra_chance=0.6, grama_chance=0.4)
    geracao += 1 

    presas = []
    predadores = []

    for i in range(numero_de_presas):
        posicao = mapa.posicao_disponivel(3)
        presas.append(CriarIndividuo(gene=gene_presa, mapeamento=mapeamento_presa, tipo=3, posicao=posicao))

    for i in range(numero_de_predadores):
        posicao = mapa.posicao_disponivel(4)
        predadores.append(CriarIndividuo(gene=gene_predador, mapeamento=mapeamento_predador, tipo=4, posicao=posicao))

    imagem = Imagem(20, 20, mapa=mapa, geracao=geracao)
    imagem.imagem()