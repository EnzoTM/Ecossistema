import random

from simulacao import Simulacao

simulacao = Simulacao()

numero_de_padawans = 5

alcances = []

for i in range(numero_de_padawans):
    alcances.append(5)

genes = [None for _ in range(numero_de_padawans)]

simulacao.start_population(x_mapa=10, y_mapa=10, 
                           numero_de_padawans=numero_de_padawans, 
                           padawans_alcance=alcances, 
                           genes=genes)

