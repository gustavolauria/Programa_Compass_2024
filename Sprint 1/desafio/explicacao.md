# Descrição

-Nesse arquivo será armazenado o passo a passo, comentado e com prints, da execução do desafio da Sprint.

1. Primeiro temos o download do arquivo *dados_de_vendas*, e já aqui temos uma pequena alteração (comunicada ao SM), onde o arquivo possuia um erro em uma de suas linhas que foi alterado, e portanto sera referido a frente como dados_de_vendas_fix.

2. Temos entao a criacao do diretorio **ecommerce** onde foi inserido o arquivo *dados_de_vendas_fix*.

3. Dentro desse diretorio criamos o nosso executavel, *processamento_de_vendas* e damos permissao a ele para de fato executar.

4. Esse arquivo fara varias tarefas diferentes, como criar diretorios, copiar, renomear, comprimir e remover arquivos, e criar o nosso *relatorio.txt*, com as informacoes pedidas.

5. Agora para utilizar o cron, corrigimos alguns problemas com o codigo, como adicionar o caminho absoluto as pastas, para realizarmos o agendamento do nosso executavel.

6. Utilizando diferentes arquivos de dados, conseguimos relatorios diferentes, e criamos o executavel *consolidador_de_processamento_de_vendas*, para juntar esses diferentes relatorio em um só, o *relatorio_final*
