def get_action(result):
    #TODO
    return 0

class Younglings:
    def __init__(self, rede_neural, espaco, alcance, posicao: list, fome = 0):
        self.rede_neural =  rede_neural
        
        self.fome = fome
        self.vivo = True
        self.espaco = espaco
        self.alcance = alcance #alcance de visão
        self.posicao = posicao
        self.alcance = alcance

        self.surroundings = self.espaco.surroundings(posicao, alcance) 

        self.sensores = []
        self.sensores.append(self.fome)

        for i in range(alcance):
            for j in range(alcance):
                self.sensores.append(self.surroundings[i][j])

    def action(self):
        action = get_action(self.rede_neural.predict(self.sensores))

    