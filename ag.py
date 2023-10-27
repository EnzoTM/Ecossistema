import random

from simulacao import Simulacao

simulacao = Simulacao()

numero_de_padawans = 3

alcances = []

for i in range(numero_de_padawans):
    alcances.append(5)

genes = [None for _ in range(numero_de_padawans)]

simulacao.start_population(x_mapa=5, y_mapa=5, 
                           numero_de_padawans=numero_de_padawans, 
                           padawans_alcance=alcances, 
                           genes=genes)

simulacao.espaco.printar_mapa()

print()
simulacao.start_simulation(30)
print()
print()

simulacao.espaco.printar_mapa()