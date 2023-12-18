# Sistemas Evolutivos - USP
## Projeto - Simulação de um ecossistema

<p><strong>se der colocar um gif do ecossistema, uma print, não sei</strong></p>

<br>
<p><strong>Documentação:</strong> https://docs.google.com/document/d/1yNXUO-0nRKN0PhTbKsiD1S7UCiqhEQIHms1Df-uPZqw/edit?usp=sharing</p>

<br>

<b>Integrantes do grupo:</b>
<ul>
  <li>Caue Paiva Lira: https://github.com/caue-paiva</li>
  <li>Enzo Tonon Morente: https://github.com/EnzoTM</li>
  <li>João Pedro Alves Notari Godoy: https://github.com/joaopgodoy</li>
  <li>Letícia Barbosa Neves: https://github.com/LeticiaBN</li>
  <li>Ayrton da Costa Ganem Filho: https://github.com/A1RT0N </li>
</ul>

<br>

<b>Professor:</b>
<br>
<ul>
  <li>Simões: https://gitlab.com/simoesusp</li>
</ul>

<br>
<br>

<b>As bibliotecas utilizadas foram:</b>
<ul>
  <li>Matplotlib: biblioteca usada para plotar o gráfico</li>
  <li>Pygame: usada para fazer a parte visual do ecossistema</li>
</ul>


<br>
<h3>Sobre o projeto:</h3>
O projeto é uma simulação de um ecossistema contendo predador, presa e grama. Nesse caso, o predador é carnívoro e a presa é herbívora, ou seja, o predador come apenas a presa e a presa come apenas a grama.

<br>

O método de mutação escolhido foi a mutação variada, em que um locus é aleatoriamente escolhido e alterado.
O método de cruzamento para gerar a nova população consiste em matar a metade da população com o menor fitness e utilizar a melhor metade para cruzar. Dessa forma, cada individuo da melhor metade irá cruzar com o melhor de todos, gerando um gene em que cada locus tem 80% de chance de ser o do melhor de todos e 20% de ser do outro individuo.

<br>

<h3>A simulação é feita da seguinte forma:</h3>

  Após criar o mapa 50x50 com as gramas (40% do mapa) e inserir as 40 presas e 40 predadores, todos tem 50 ações para realizar. O fitness e definido pelo sucesso na obtenção de comida e sobrevivência, sendo que quanto maior o fitness, maior a chance de ser o melhor de todos e passar os genes para a próxima geração.
- Fitness da presa: ela ganha 2 pontos por comer e perde 0,5 se não comer
- Fitness do predador: ele ganha 10 pontos por comer e perde 0,5 se não comer
Dessa forma, as presas e os predadores estão em constante evolução para conseguir aumentar seu fitness e aumentar a sobrevivência de sua população no ecossistema, como é possível observar no gráfico gerado abaixo.
Além disso, ao fim de cada ação as gramas renascem no mapa e as presas mortas renascem em outra posição e têm sua pontuação zerada.

<br>

<div align="center">
  <img src="https://github.com/EnzoTM/Ecossistema/blob/main/Simula%C3%A7%C3%A3o%20do%20Ecossistema/graficos/0.png?raw=true">
</div>
