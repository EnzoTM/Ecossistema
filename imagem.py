import sdl2
import sdl2.ext
from sdl2 import SDL_Rect, SDL_SetRenderDrawColor, SDL_RenderFillRect

# PROTÓTIPO --- NÃO TÁ CONECTADO NO CÓDIGO AINDA

def draw_circle(renderer, center_x, center_y, radius, color):
    x = radius
    y = 0
    p = 1 - radius

    def draw_symmetric_points(cx, cy, x, y):
        points = [
            (cx + x, cy + y),
            (cx - x, cy + y),
            (cx + x, cy - y),
            (cx - x, cy - y),
            (cx + y, cy + x),
            (cx - y, cy + x),
            (cx + y, cy - x),
            (cx - y, cy - x)
        ]
        for point in points:
            renderer.draw_point(point, color)

    while x >= y:
        draw_symmetric_points(center_x, center_y, x, y)
        y += 1
        if p <= 0:
            p += 2 * y + 1
        else:
            x -= 1
            p += 2 * (y - x) + 1
        draw_symmetric_points(center_x, center_y, x, y)


def run_simulation():
    # Inicializa a SDL2
    sdl2.ext.init()

    # Cria uma janela
    window = sdl2.ext.Window("Ecossistema", size=(1900, 1000))
    window.show()

    # Cria um renderizador para desenhar na janela
    renderer = sdl2.ext.Renderer(window)

    # Definindo cores
    BLACK = sdl2.ext.Color(0, 0, 0)
    RED = sdl2.ext.Color(255, 0, 0)   # Predador
    GREEN = sdl2.ext.Color(0, 255, 0) # Presa
    BLUE = sdl2.ext.Color(0, 0, 255)  # Obstáculo
    WHITE = sdl2.ext.Color(255, 255, 255) # Área Livre

    running = True
    while running:
        # Processa eventos
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False

        # Clear the screen
        renderer.clear(BLACK)

        # Desenha os elementos
        # Predador - um círculo vermelho
        draw_circle(renderer, 400, 300, 30, RED)

        # Presa - um quadrado verde
        SDL_SetRenderDrawColor(renderer.sdlrenderer, GREEN.r, GREEN.g, GREEN.b, GREEN.a)
        green_rect = SDL_Rect(200, 150, 50, 50)
        SDL_RenderFillRect(renderer.sdlrenderer, green_rect)

        # Obstáculo - um quadrado azul
        SDL_SetRenderDrawColor(renderer.sdlrenderer, BLUE.r, BLUE.g, BLUE.b, BLUE.a)
        blue_rect = SDL_Rect(600, 450, 50, 50)
        SDL_RenderFillRect(renderer.sdlrenderer, blue_rect)

        # Área Livre - um quadrado branco
        SDL_SetRenderDrawColor(renderer.sdlrenderer, WHITE.r, WHITE.g, WHITE.b, WHITE.a)
        white_rect = SDL_Rect(100, 450, 50, 50)
        SDL_RenderFillRect(renderer.sdlrenderer, white_rect)

        # Atualiza a janela
        renderer.present()

    # Limpa recursos antes de sair
    sdl2.ext.quit()

if __name__ == "__main__":
    run_simulation()
