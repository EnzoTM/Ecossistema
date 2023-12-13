from mapa.mapa import Mapa

import time

mapa = Mapa(10, 10, terra_chance=1, grama_chance=0, obstaculo_chance=0)

while(True):
    input()
    mapa.posicao_disponivel(1)
    mapa.printar_mapa()

    print(end="\n\n\n")