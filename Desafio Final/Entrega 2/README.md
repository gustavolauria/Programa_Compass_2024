# Descrição

- Nesse arquivo será armazenado o passo a passo da primeira entrega do **Desafio Final**

- Para ter acesso aos arquivos e prints da execução dessa etapa: [Entrega II](../../Sprint%207/desafio/README.md)


## Passo a Passo

1. O primeiro passo para o começo desse desafio é definir qual seria os dados que eu gostaria de adicionar, através da API do TMDB. Para a minha análise, seria relevante obter os gastos e lucros dos filmes de Sci-Fi e Fantasia, e por isso, eu fui atras do método *movie_details* da API, que me retorna, além de outras informações, o orçamento e o custo de cada filme. 
<img src="img/tmdb.jpg" width="60%">

2. Como a API possui certas limitações com o método escolhido, foi necessário limitar um pouco o escopo das informações buscadas. Cada chamada da API só pode retornar a informação de 1 filme, e como o nosso arquivo *movies.csv* tem aproximadamente 240 mil filmes únicos, para obter as informações necessárias de **todos** os filmes, seriam necessárias 240 mil chamadas a API, o que infelizmente não é possível. Dada essa informação, foi preciso se limitar apenas ao filmes de Sci-Fi e Fantasia, e desses genêros, apenas os filmes que possuiam certa relevância(número de votos acima de 1000), afim de aumentar as chances da database do TMDB possuir informações sobre o mesmo.

3. Com as nossas restrições já estabelecidas, podemos começar a programar de fato. Começando pela programação local, construimos uma função que, dada as restrições, nos retorna a lista de ids de filmes que iremos buscar na API. Fazemos então um loop, que percorre a nossa lista de ids e retorna a informação de cada filme, armazenando esse retorno no formato **json**, e fazendo com que cada retorno seja agrupado, de maneira que 1 arquivo json contenha o resultado de 100 filmes.

4. Agora que o nosso código esta funcionando localmente, é hora de passar tudo para a AWS, utilizando o AWS Lambda para isso. Configuramos a nossa função Lambda para rodar em até 15 min e com 2000 MB de memória, já que o nosso programa é um pouco demorado, e pode demandar bastante. Fazemos também algumas alterações no código para adapta-lo ao Lambda.

5. Finalmente, ao rodar a nossa função, temos os nosso arquivos **json** armazenados corretamente no nosso bucket do S3, concluindo a etapa 2 do Desafio Final.
<img src="img/log_inicial.jpg" width="60%">

<img src="img/log_final.jpg" width="60%">

<img src="img/jsons.jpg" width="60%">
