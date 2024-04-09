# Descrição

- Nesse arquivo será armazenado o passo a passo, comentado e com prints, da execução do laboratório 3 desta Sprint.


## Passo a Passo

1. Para esse laboratório, iremos criar uma função lambda que interage com o bucket criado previamente. Ao criarmos nossa função, vemos que o Python 3.7 não é mais suportado pela AWS, e portanto teremos que trabalhar com o Python 3.9 . 

2. Após criada, inserimos na nossa função o código que deverá ser rodado. Ele nos retorna um status, e o número de linhas do arquivo. <img src="img/funçao.jpg" width="60%">

3. Ao executar a nossa função, recebemos um erro de 'import'. Para corriji-lo precisaremos criar um **Layer**. Utilizando o Docker, criamos uma [Dockerfile](arquivos/Dockerfile), e fazemos o 'build' e o 'run' de um container Docker, *amazonlinuxpython* <img src="img/container.jpg" width="60%">

4. Executamos alguns comandos, para termos os arquivos do container compactados na pasta [minha-camada-pandas.zip](arquivos/minha-camada-pandas.zip), fazemos uma cópia desse arquivo para nossa máquina local e depois o upload para o nosso bucket do S3.

5. Podemos finalmente criar o nosso **Layer**, compatível com o Python 3.9 . <img src="img/layer.jpg" width="60%">

6. Ao adicionar o layer a nossa função lambda, temos finalmente o resultado esperado. <img src="img/resultado.jpg" width="60%">

7. No final, fazemos a limpeza tanto do nosso bucket do S3, quanto da nossa função lambda, para minizarmos qualquer custo. <img src="img/limpeza_bucket.jpg" width="60%">

<img src="img/limpeza_lambda.jpg" width="60%">