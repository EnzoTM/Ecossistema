from mapa.mapa import Mapa

mapa = Mapa(10, 10, obstaculo_chance=0, terra_chance=0.5, grama_chance=0.5)

posicao = mapa.posicao_disponivel(3)

while(1):
    mapa.printar_mapa()

    comando = input("Digita: ")

    if comando == "w":
        posicao, _ = mapa.make_action(postion=posicao, action=1)

    if comando == "s":
        posicao, _ = mapa.make_action(postion=posicao, action=2)

    if comando == "d":
        posicao, _ = mapa.make_action(postion=posicao, action=3)

    if comando == "a":
        posicao, _ = mapa.make_action(postion=posicao, action=4)