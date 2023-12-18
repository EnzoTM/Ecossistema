from mapa.mapa import Mapa
from individuos.individuo import CriarIndividuo
import numpy as np

mapa = Mapa(10, 10, obstaculo_chance=0, terra_chance=0.5, grama_chance=0.5)

gene = [{'input_size': 4, 'output_size': 5, 'weights': [[-0.026142214261745303, 0.3457903390875814, -0.18328792971248792, 0.2456399056131861], [-0.15255064813940172, 0.5757960358972001, -7.994507137834041e-05, -0.12924164054035348], [0.09149397435841866, -0.23594360926769736, -0.1741884163231752, 0.10801259074731387], [-0.1807459008070014, 0.12954212532178677, 0.06809554062216813, -0.6097528102488722], [0.17558853356062523, 0.03756016188298296, -0.4600606085586968, -0.056748449149545285]], 'weights_shape': [5, 4], 'bias': [[0.4889228026055321], [-0.11185147178101716], [0.10128525225168866], [0.05282939284796215], [0.08869544714441663]], 'bias_shape': [5, 1], 'activation_function': 'Tanh'}, {'input_size': 5, 'output_size': 1, 'weights': [[-0.184272941373001, -0.45754029665160306, -0.0036519127902054733, -0.308211942309866, -0.09290530130026783]], 'weights_shape': [1, 5], 'bias': [[-0.13724268650768762]], 'bias_shape': [1, 1], 'activation_function': 'Tanh'}]

posicao = mapa.posicao_disponivel(3)
individuo = CriarIndividuo(gene=gene, posicao=posicao, tipo=3, modelo=None)

while(1):
    mapa.printar_mapa()

    comando = input("Digita: ")

    inputs = mapa.inputs(individuo.posicao) #pegar os inputs para esse individuo

    predicao = individuo.network.predict(inputs) #fazer a predicao

    #ver qual ação deve ser feita
    acao = np.argmax(predicao)

    #fazer a ação
    nova_posicao, resultado = mapa.make_action(acao, individuo.posicao)

    #---------------------Resultado da ação---------------------
    individuo.posicao = nova_posicao #atualizar a posição