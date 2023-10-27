from objetos.mapa import Mapa
from objetos.younglings import Younglings

from rede_neural.rede_neural import Network, Dense, get_shapes

model_architecture_padawans = [

    Dense(26, activation_function="ReLU", input_shape=(26, 1)),
    Dense(52, activation_function="ReLU"),
    Dense(52, activation_function="ReLU"),
    Dense(5, activation_function="Sigmoid", input_shape=(5, 1))

]

model_shape_padawans = get_shapes(model_architecture_padawans)

class Simulacao():
    def __init__(self) -> None:
        pass

    def start_population(self, x_mapa, y_mapa, numero_de_padawans, padawans_alcance: list, genes: list):
        self.espaco = Mapa(x_mapa, y_mapa)

        self.padawans = []

        for i in range(numero_de_padawans):
            self.padawans.append(Younglings(model_architecture=model_architecture_padawans, 
                                            espaco=self.espaco, alcance=padawans_alcance[i],
                                            posicao=self.espaco.posicao_disponivel(3),
                                            shapes=model_shape_padawans,
                                            gene=genes[i]))
    
    def start_simulation(self, numero_de_geracoes):
        for i in range(numero_de_geracoes):
            for padawan in self.padawans:
                action = padawan.action()