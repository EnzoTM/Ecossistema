import pygame
from neat.mapa.mapa import Mapa

class Imagem():
    def __init__(self, x_mapa: int, y_mapa: int, mapa: list):
        self.x = x_mapa
        self.y = y_mapa
        self.mapa = mapa

    def imagem(self):
        pygame.init()
        # Configurações da tela
        screen_width = 500
        screen_height = 400
        screen = pygame.display.set_mode((screen_width, screen_height))
        
        # Carregar imagens
        grama_image = pygame.image.load('img/floor.png')
        grama_image = pygame.transform.scale(grama_image, (int(screen_width / self.x), int(screen_height / self.y)))

        earth_image = pygame.image.load('img/earth.png')
        earth_image = pygame.transform.scale(earth_image, (int(screen_width / self.x), int(screen_height / self.y)))

        rock_image = pygame.image.load('img/rock.png')
        rock_image = pygame.transform.scale(rock_image, (int(screen_width / self.x), int(screen_height / self.y)))

        # Cores
        Water = (0, 0, 255)  # Cor azul água

        # Loop principal
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            escala_x = screen_width / self.x
            escala_y = screen_height / self.y

            for y in range(self.y):
                for x in range(self.x):
                    tipo_terreno = self.mapa[y][x]
                    if tipo_terreno == 1:  # Obstáculo
                        screen.blit(rock_image, (x * escala_x, y * escala_y))
                    elif tipo_terreno == 0:  # Espaço livre
                        screen.blit(earth_image, (x * escala_x, y * escala_y))
                    elif tipo_terreno == 2:  # Grama
                        screen.blit(grama_image, (x * escala_x, y * escala_y))
                    elif tipo_terreno == 3:  # Água
                        pygame.draw.rect(screen, Water, (x * escala_x, y * escala_y, escala_x, escala_y))

            pygame.display.flip()  # Atualiza a tela

# Terra - espaço livre = 0
# Obstáculo = 1
# Grama = 2
# Predador = 3
# Presa = 4

mapa = Mapa(4, 4)
imagem = Imagem(4, 4, mapa.mapa)

mapa.printar_mapa()

imagem.imagem()



# PROBLEMAS: O ANIMAL PODE FICAR PRESO CERCADO POR PEDRA - CONSERTAR ISSO EM MAPA