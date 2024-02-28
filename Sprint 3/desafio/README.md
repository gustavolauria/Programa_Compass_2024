# Descrição

- Nesse arquivo será armazenado o passo a passo, comentado e com prints, da execução do desafio da Sprint e todos os códigos fonte utilizados.

- O diretório **arquivos** conterá todos os arquivos gerados no desafio, sejam eles de texto *(.txt)*, de codigo fonte *(.sh)* , etc.
- O diretório **img** conterá todos os prints tirados ao longo da execução do desafio.

## Passo a Passo

1. Primeiro baixamos o arquivo no qual iremos trabalhar *googleplaystore.csv*, e realizamos um tratamento simples dele, retirando linhas duplicadas, e o cifrão '$' da coluna de preços para facilitar nossa futura análise. Salvamos o arquivo tratado como *arquivo_limpo*, e ele será utilizado no nossos futuros scripts.

2. Para o nossa primeira análise, faremos um grafico de barras utilizando a biblioteca **matplotlib** dos aplicativos com maior número de instalação.

3. Nosso segundo programa faz um gráfico de pizza mostrando as categorias de apps presentes no nosso database, e sua porcentagem. Possui um pequeno tratamento em uma linha que estava errada no nosso banco, e categoriza as categorias que possuem menos de 2% do total como **Outros**, a fim de melhorar a visualização do gráfico.

4. Terceiro script nos retorna o aplicativo mais caro do nosso database.

5. O quarto retorna a quantidade de aplicativos que são **Mature 17+**.

6. A quinta análise retorna os 10 apps com maior número de avaliações, ordenados de forma decrescente.

7. O sexto programa retorna o aplicativo com maior número de avaliações e também uma lista de 10 aplicativos que possuem a maior nota da GooglePlayStore que é 5.0.

8. O sétimo script retorna um gráfico de linhas que mostra a porcentagem da classificação dos aplicativos, filtrando apenas as classificações que possuem pelo menos 1% de relevância, tornando o gráfico mais fácil de ser entendido.

9. O último programa retorna um gráfico de dispersão dos diversos ratings que os aplicativos possuem, numa faixa do 3.25 até o 5.0.