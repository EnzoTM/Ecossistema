# Simulação de um ecossistema 

Documentação: https://docs.google.com/document/d/1yNXUO-0nRKN0PhTbKsiD1S7UCiqhEQIHms1Df-uPZqw/edit?usp=sharing

As bibliotecas utilizadas foram:
- Matplotlib: biblioteca usada para plotar o gráfico
- Pygame: usada para fazer a parte visual do ecossistema

O projeto é uma simulação de um ecossistema contendo predador, presa e grama. Nesse caso, o predador é carnívoro e a presa é herbívora, ou seja, o predador come apenas a presa e a presa come apenas a grama.

O método de mutação escolhido foi a mutação variada, em que um locus é aleatoriamente escolhido e alterado.
O método de cruzamento para gerar a nova população consiste em matar a metade da população com o menor fitness e utilizar a melhor metade para cruzar. Dessa forma, cada individuo da melhor metade irá cruzar com o melhor de todos, gerando um gene em que cada locus tem 80% de chance de ser o do melhor de todos e 20% de ser do outro individuo.

A simulação é feita da seguinte forma:
Após criar o mapa com as gramas e inserir as presas e predadores, todos tem X ações para realizar. O fitness e definido pelo sucesso na obtenção de comida e sobrevivência, sendo que quanto maior o fitness, maior a chance de ser o melhor de todos e passar os genes para a próxima geração.
- Fitness da presa: ela ganha 2 pontos por comer e perde 0,5 se não comer
- Fitness do predador: ele ganha 10 pontos por comer e perde 0,5 por não comer
Dessa forma, as presas e os predadores estão em constante evolução para conseguir aumentar seu fitness e aumentar a sobrevivência de sua população no ecossistema, como é possível observar nos gráficos gerados:

INSERIR GRAFICOS AQUI


Além disso, ao fim de cada ação as gramas renascem no mapa e as presas mortas renascem em outra posição, além de ter sua pontuação zerada.
O mapa inicial tem tamanho 50x50, cada presa/predador tem 50 ações e existem 40 presas e 40 predadores. Além disso, 40% do mapa terá grama para que as presas possam comer.

