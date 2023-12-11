from simulacao import Simulacao

gene = [[[[0, 0], [4, None], [5, None], [6, None], [7, None]], [[1, 0], [4, None], [5, None], [6, None], [7, None]], [[2, 0], [4, None], [5, None], [6, None], [7, None]], [[3, 0], [4, None], [5, None], [6, None], [7, None]]],
        [[[4, None]], [[5, None]], [[6, None]], [[7, None]]]]

simulacao = Simulacao()

simulacao.StartSimulation(numero_de_geracoes=300, numero_de_acoes=40, numero_de_individuos=100, gene_individuo=gene)

simulacao.Results()