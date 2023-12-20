from mapa.mapa import Mapa
from individuos.individuo import CriarIndividuo
from copy import copy

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

numero_de_presas = 3
numero_de_predadores = 3

if numero_de_predadores > numero_de_presas: tamanho = numero_de_predadores
else: tamanho = numero_de_presas

while(True):
    mapa = Mapa(10, 10, obstaculo_chance=0, terra_chance=0.6, grama_chance=0.4)

    presas = []
    predadores = []

    for i in range(numero_de_presas):
        posicao = mapa.posicao_disponivel(3)
        presas.append(CriarIndividuo(gene=gene_presa, mapeamento=mapeamento_presa, tipo=3, posicao=posicao))

    for i in range(numero_de_predadores):
        posicao = mapa.posicao_disponivel(4)
        predadores.append(CriarIndividuo(gene=gene_predador, mapeamento=mapeamento_predador, tipo=4, posicao=posicao))

    
    flag = 0
    
    while(True):
        if flag:
            break

        for i in range(tamanho):
            comando = input()

            if comando == '1': 
                flag = 1
                break #reinicia tudo

            tmp = copy(mapa.presas_mortas) #cópia da lista de presas mortas

            for h in range(len(tmp)): #para cada presa morta
                posicao = mapa.posicao_disponivel(3) #pegar uma novoa posição para a presa spawnar

                for j in range(len(presas)):
                    if presas[j].posicao == tmp[h]: #achar qual q é a presa q morreu
                        presas[j].posicao = posicao #atualizar sua posição

                        presas[j].quantidade = 0 #zerar a pontuação dela, pois ela morreu

                        mapa.presas_mortas.remove(tmp[h]) #remover da lista de presas mortas

            mapa.printar_mapa()
            print("\n\n")
            
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