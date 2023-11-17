import pygame  
from objetos.mapa import Mapa

class Imagem():
    def __init__(self, x_mapa: int, y_mapa: int, mapa: list):
        self.x = x_mapa
        self.y = y_mapa
        self.mapa = mapa
        
    def imagem(self):
        
        pygame.init()
        # Configurações da tela
        screen_width = 1900
        screen_height = 1000
        screen = pygame.display.set_mode((screen_width, screen_height))

        # Cores
        BLACK = (0, 0, 0) # Teoricamente é pra ser a área livre mas não sei se tá sendo
        RED = (255, 0, 0)   # Predador
        GREEN = (0, 255, 0) # Presa
        BLUE = (0, 0, 255)  # Livre


        # Inicializa o mapa e a simulação

        # Loop principal
        running = True

        while running:
            # Processa eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Limpar tela
            # screen.fill(BLACK)


            # Renderiza o mapa e obstáculos
            escala_x = screen_width / self.x_mapa
            escala_y = screen_height / self.y_mapa
            for y in range(self.y_mapa):
                for x in range(self.x_mapa):
                    tipo_terreno = self.mapa[y][x]
                    if tipo_terreno == 1:  # Exemplo: 1 representa um obstáculo
                        pygame.draw.rect(screen, BLUE, (x * escala_x, y * escala_y, escala_x, escala_y)) # Obstáculo em azul
                    elif tipo_terreno ==  0:
                        pygame.draw.rect(screen, BLACK, (x * escala_x, y * escala_y, escala_x, escala_y))
                    elif tipo_terreno == 2:
                        pygame.draw.ellipse(screen, GREEN, (x * escala_x, y * escala_y, escala_x, escala_y))
                    # elif tipo_terreno == 3:
                    #     pygame.draw.circle(screen, RED, )

            pygame.display.flip()
            pygame.time.delay(2000)  # 2 segundos
            


# Terra - espaço livre = 0
# Obstáculo = 1
# Grama = 2
# Predador = 3
# Presa = 4

mapa = Mapa(4, 4)
mapa.printar_mapa()
# Imagem(4,4, mapa.mapa)