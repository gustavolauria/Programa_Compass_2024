# Descrição

- Nesse arquivo será armazenado o passo a passo da primeira entrega do **Desafio Final**

- Para ter acesso aos arquivos e prints da execução dessa etapa: [Entrega I](../../Sprint%206/desafio/README.md)

## Análise

1. O primeiro passo para o começo desse desafio é definir qual será o tipo de análise que pretende ser feita. A análise será feita em torno dos temas Sci-Fi/Fantasia, e de acordo com as informações que futuramente iremos obter dos dados, pretendemos chegar a algumas conclusões em relação aos seguintes questionamentos:

- Os filmes de Sci-Fi/Fantasia são mais predominantes hoje em dia (dado o aumento tecnológico) ? 

- Se sim, esse maior interesse nos temas, pode ser explicado por outros fatores(aumento da indústria como um todo) ?
- Se sim, esse aumento veio a custo da qualidade (a média de rating desses filmes aumentou ? diminui ?)
- Se sim, a partir de que momento (década de 70 ? 80 ?) ? 
- Se não, o sucesso do tema é devido as grandes franquias (Star Wars, Senhor dos Aneis) ?
- Se não, existe pelo menos um aumento em relação a outros genêros (Romance, Drama, Terror) ? 

## Passo a Passo

1. Criamos o bucket que irá armazenar os nossos dados *data-lake-desafio-final*

2. Fazemos a configuração das nossas credenciais na máquina local utilizando o AWS CLI. Elas serão necessárias na hora de subirmos os arquivos para o bucket do S3.

3. Montamos o nosso script *carregar.py*, que fará o upload dos arquivos para o nosso bucket no S3, e montamos também o *dockerfile*, que fará essa tranferência.

4. Utilizando então o Docker, criamos uma imagem do nosso programa e dos nossos arquivos, e rodamos num volume que possua as nossas credenciais AWS, para que o Docker tenha acesso a AWS.

5. Entrando agora na AWS, e acessando o S3, podemos ver o nosso bucket *data-lake-desafio-final*, com os arquivos *movies.csv* e *series.csv* nas devidas pastas.