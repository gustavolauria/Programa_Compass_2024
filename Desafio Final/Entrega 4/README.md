# Descrição

- Nesse arquivo será armazenado o passo a passo da primeira entrega do **Desafio Final**

- Para ter acesso aos arquivos e prints da execução dessa etapa: [Entrega IV](../../Sprint%209/desafio/README.md)

## Passo a Passo

1. Nesse desafio, fizemos a camada **Refined** do nosso *data-lake*, que é a camada que possui as tabelas que iremos analisar futuramente, no modelo dimensional.

2. Para comecar, fizemos a nossa modelagem dimensional, tentando separar no nosso *Fato_Movies* os elementos quantitativos que o compõem, por exemplo, o *budget*, *revenue*, *profits*, etc, e as nossas dimensões, *Dim_Time* e *Dim_Sub-Genre* que vão conter os atributos qualitativos. 

<img src="../../Sprint%209/desafio/img/modelagem.png" width="60%">

3. Após completarmos a modelagem, podemos passar para o código, que implementará de fato as nossas tabelas. Comecamos fazendo ele localmente usando o Google Colab, e posteriormente, quando tudo já estava encaminhado, passamos para o **AWS GLUE**.

4. O nosso código vai criar as nossas 3 tabelas, o *Fato* e as duas *Dimensões*, e exporta-las em formato parquet para a nossa camada **Refined** do nosso data-lake.

<img src="../../Sprint%209/desafio/img/fato_movie.jpg" width="60%">

<img src="../../Sprint%209/desafio/img/dim_time.jpg" width="40%">

<img src="../../Sprint%209/desafio/img/dim_sub-genre.jpg" width="40%">

5. Com a nossa camada criada, podemos então criar e rodar um *Crawler*, que pegará toda a informação das nossas tabelas e usará para popular o **AWS Data Catalog**, com as nossas tabelas.

<img src="../../Sprint%209/desafio/img/crawler_datalake.jpg" width="60%">

<img src="../../Sprint%209/desafio/img/tabelas.jpg" width="60%">