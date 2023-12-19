# Sistemas Evolutivos - USP
## Projeto - Simulação de um ecossistema

<br>
<p><strong>Documentação:</strong> https://docs.google.com/document/d/1yNXUO-0nRKN0PhTbKsiD1S7UCiqhEQIHms1Df-uPZqw/edit?usp=sharing</p>
<br>

<br>
<p><strong>Requirements:</strong> 
pygame 2.5.2
matplotlib==3.8.2
numpy==1.26.2
</p>
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
<ul>
  <li>Simões: https://gitlab.com/simoesusp</li>
</ul>

<br>

<b>As bibliotecas utilizadas foram:</b>
<ul>
  <li>Matplotlib: biblioteca usada para plotar o gráfico</li>
  <li>Pygame: usada para fazer a parte visual do ecossistema</li>
</ul>

<br>
<h3>Sobre o projeto:</h3>
<p></p>O projeto é uma simulação de um ecossistema contendo predador, presa e grama. Nesse caso, o predador é carnívoro e a presa é herbívora, ou seja, o predador come apenas a presa e a presa come apenas a grama. </p>
<p>A tomada de decisões da presa e do predador é feita a partir de uma tabela verdade. A presa terá 3 inputs, sendo eles: se existe comida, aliado ou inimigo perto dela, sendo que ela irá se aproximar da comida e dos aliados e se afastar dos inimigos, podendo também andar aleatóriamente ou ficar parado. Já o predador vai receber apenas 2 inputs: se existe comida ou um aliado perto dele, e irá se aproximar da comida ou do aliado, além de poder andar aleatóriamente ou ficar parado. Assim, o trabalho do AG é descobrir qual ação cada individuo deve tomar com base nos inputs atuais para aumentar seu fitness e se tornar o melhor individuo. </p>

<p>O método de mutação escolhido foi a mutação variada, em que um locus é aleatoriamente escolhido e alterado.<br>
O método de cruzamento para gerar a nova população consiste em matar a metade da população com o menor fitness e utilizar a melhor metade para cruzar. Dessa forma, cada individuo da melhor metade irá cruzar com o melhor de todos, gerando um gene em que cada locus tem 80% de chance de ser o do melhor de todos e 20% de ser do outro individuo.</p>

<br>
<h3>A simulação é feita da seguinte forma:</h3>
  <p>Após criar o mapa 50x50 com as gramas (40% do mapa) e inserir as 40 presas e 40 predadores, todos tem 50 ações para realizar. O fitness e definido pelo sucesso na obtenção de comida e sobrevivência, sendo que quanto maior o fitness, maior a chance de ser o melhor de todos e passar os genes para a próxima geração.</p>
<ul>
  <li><strong>Fitness da presa:</strong> ela ganha 2 pontos por comer e perde 0,5 se não comer</li>
  <li><strong>Fitness do predador:</strong> ele ganha 10 pontos por comer e perde 0,5 se não comer</li>
</ul>
<p>Dessa forma, as presas e os predadores estão em constante evolução para conseguir aumentar seu fitness e aumentar a sobrevivência de sua população no ecossistema. Como é possível observar no gráfico gerado abaixo vemos que conforme o fitness da presa aumenta o do predador diminuiu e vice-versa. Também podemos ver essas "ondas", onde a presa está com um fitness baixo e encontra uma nova estratégia (evoluiu), aumentando o seu fitness e tornando o fitness dos predadrores baixo o que faz com que eles evoluam tornando o fitness da presa baixo e assim por diante. <br> Esse comportamento é esperado, pois na natureza se temos um predador que está comendo muito as presas as mesmas precisam de uma nova estratégia para poder escapar deles fazendo com que os predadores não comam mais resultando com que eles evoluam para poder comer a presa e assim se gera esse loop.</p>

<br>

<div align="center">
  <img src="https://github.com/EnzoTM/Ecossistema/blob/main/Simula%C3%A7%C3%A3o%20do%20Ecossistema/graficos/0.png?raw=true">
</div>
