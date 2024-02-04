# Descrição

-Nesse arquivo será armazenado o passo a passo, comentado e com prints, da execução do desafio da Sprint.

## Passo a Passo

1. Primeiro, realizamos o download do arquivo *dados_de_vendas*. Já neste ponto, observamos uma pequena alteração (comunicada ao SM), onde o arquivo possuía um erro em uma de suas linhas, o qual foi corrigido. Portanto, será referido daqui para frente como *dados_de_vendas_fix*.

2. Em seguida, procedemos com a criação do diretório **ecommerce**, onde inserimos o arquivo *dados_de_vendas_fix*.

3. Dentro desse diretório, criamos nosso executável, *processamento_de_vendas*, e concedemos permissão para sua execução efetiva.

4. Este arquivo realizará diversas tarefas, tais como criar diretórios, copiar, renomear, comprimir e remover arquivos, além de gerar nosso *relatorio.txt* com as informações solicitadas.

5. Agora, para utilizar o **cron**, corrigimos alguns problemas no código, como adicionar o caminho absoluto às pastas, a fim de agendar a execução do nosso executável.

6. Utilizando diferentes arquivos de dados, obtemos relatórios distintos, e desenvolvemos o executável *consolidador_de_processamento_de_vendas* para reunir esses relatórios diversos em um único documento, o *relatorio_final*.
