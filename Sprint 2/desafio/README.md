# Descrição

- Nesse arquivo será armazenado o passo a passo, comentado e com prints, da execução do desafio da Sprint e todos os códigos fonte utilizados.

- O diretório **arquivos** conterá todos os arquivos gerados no desafio, sejam eles de texto *(.txt)*, de codigo fonte *(.sh)* , etc.
- O diretório **img** conterá todos os prints tirados ao longo da execução do desafio.

## Passo a Passo

1. Primeiro baixamos o arquivo no qual iremos trabalhar *concessionaria.zip* e o descopactamos para termos acesso ao .sqlite

2. Agora com o .sqlite, temos dentro dele a tabela *tb_locacoes*, contendo as informacoes sobre uma locadora de carros. Analisando ela e normalizando para o modelo relacional, criamos 4 tabelas do 0, a tabela *locacao*, *carros*, *clientes* e *vendedores*.

3. Populamos as 4 tabelas criadas com as informações fornecidas pela tabela original, *tb_locacoes*, ja com todas as tabelas normalizadas.

4. Para fazermos agora o modelo dimensional utilizamos as **views**, para criarmos o *fato_locacao*, e suas 4 dimensões, *dim_tempo*, *dim_clientes*, *dim_carros*, *dim_vendedores*.