import pygame  
from objetos.mapa import Mapa
from objetos.younglings import Younglings
from simulacao import Simulacao
from ag import numero_de_padawans, genes, x_mapa, y_mapa, simulacao # NÃO TO CONSEGUINDO IMPORTAR ALCANCES

# Inicializar Pygame
pygame.init()


# Configurações da tela
screen_width = 1900
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

# Cores
BLACK = (0, 0, 0) # Teoricamente é pra ser a área livre mas não sei se tá sendo
RED = (255, 0, 0)   # Predador
GREEN = (0, 255, 0) # Presa
BLUE = (0, 0, 255)  # Obstáculo

# Inicializa o mapa e a simulação

mapa = Mapa(x_mapa, y_mapa)
simulacao = Simulacao()
padawans_alcance = [5] * numero_de_padawans # NÃO TO CONSEGUINDO IMPORTAR ALCANCES GRRRRRRRRRRRRRRR - VOU TE PEGAR ENZO
simulacao.start_population(x_mapa, y_mapa, numero_de_padawans, padawans_alcance, genes)

# Loop principal
running = True
geracao_atual = 0
numero_de_geracoes = 5

while running and geracao_atual < numero_de_geracoes:
    # Processa eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpar tela
    screen.fill(BLACK)
    
    geracao_atual += 1
    
    for padawan in simulacao.padawans:   ## ERA PRA ATUALIZAR AQUI MAS NÃO ESTÁ ATUALIZANDO  -- ATUALIZAR
        if padawan.vivo:
            action = padawan.action()
            result = simulacao.espaco.make_action(action, padawan.posicao)

            if padawan.update(result) == -1:
                simulacao.espaco.update_by_death(padawan.posicao)

    # Atualiza o ambiente após cada ação
    simulacao.espaco.atualizar()

    # Renderiza o mapa e obstáculos
    escala_x = screen_width / x_mapa
    escala_y = screen_height / y_mapa
    for y in range(y_mapa):
        for x in range(x_mapa):
            tipo_terreno = mapa.mapa[y][x]
            if tipo_terreno == 1:  # Exemplo: 1 representa um obstáculo
                pygame.draw.rect(screen, BLUE, (x * escala_x, y * escala_y, escala_x, escala_y)) # Obstáculo em azul
                


    # Renderiza as presas
    for padawan in simulacao.padawans:
        if padawan.vivo:
            x, y = padawan.posicao
            pygame.draw.circle(screen, GREEN, (int(x * escala_x), int(y * escala_y)), 5)



    pygame.display.flip()
    pygame.time.delay(2000)  # 2 segundos
    
    # Verificar se a simulação deve continuar
    if geracao_atual >= numero_de_geracoes:
        running = False
    

pygame.quit()



# QUESTÕES A SE PENSAR:
# --> 1: Não sei o que é essa matriz que é gerada então talvez esteja dando problema
# --> 2: Não sei por que algumas pressas estão sendo geradas nas bordas dos obstáculos -> mudar isso
# --> 3: PRECISA ATUALIZAR CORRETAMENTE AS POSICOES DO PADAWAN - LINHA 46
# --> 4: NÃO TO CONSEGUINDO IMPORTAR ALCANCES  -- linha 6
# --> 5: Pensarei primeiro em funcionabilidade e depois em simplicidade para passar pro mojo. Posso tentar ver depois novas bibliotecas gráficas
# --> 6: Não irei usar SDL por motivos de não sei se tem no mojo e tá mt chato
