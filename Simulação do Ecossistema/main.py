from simulacao import Simulacao

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

gene_predador = [None] * 4
gene_presa = [None] * 8

simulacao = Simulacao()

simulacao.StartSimulation(numero_de_acoes=50, numero_de_predadores=40, gene_predador=gene_predador, mapeamento_predador=mapeamento_predador,
                          numero_de_presas=40, gene_presa=gene_presa, mapeamento_presa=mapeamento_presa)