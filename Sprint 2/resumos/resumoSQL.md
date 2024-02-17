# Resumo SQL

### SELECT

- Recupera dados de uma tabela no banco de dados.
    ```SQL
    SELECT coluna1, coluna2 FROM tabela WHERE condição;
    ```
### DISTINCT

- Retorna valores únicos de uma coluna em uma consulta.
    ```SQL
    SELECT DISTINCT coluna FROM tabela;
    ```

### WHERE

- Filtra registros com base em condições específicas.
    ```SQL
    SELECT coluna FROM tabela WHERE condição;
    ```


### ORDER BY

- Classifica os resultados da consulta em ordem ascendente ou descendente.
    ```SQL
    SELECT coluna FROM tabela ORDER BY coluna ASC|DESC;
    ```


### LIMIT

- Restringe o número de linhas retornadas em uma consulta.
    ```SQL
    SELECT coluna FROM tabela LIMIT quantidade;
    ```

### GROUP BY

- Agrupa os resultados da consulta com base em valores comuns em uma ou mais colunas.
    ```SQL
    SELECT coluna1, coluna2, COUNT(*) FROM tabela GROUP BY coluna1, coluna2;
    ```


### HAVING

- Funciona como uma cláusula de filtro para grupos criados pelo GROUP BY.
    ```SQL
    SELECT coluna1, COUNT(*) FROM tabela GROUP BY coluna1 HAVING COUNT(*) > 10;
    ```

### LEFT JOIN

- Retorna todas as linhas da tabela à esquerda e as correspondentes da tabela à direita. Se não houver correspondência, retorna NULL para as colunas da tabela à direita.
    ```SQL
    SELECT * FROM tabela_esquerda LEFT JOIN tabela_direita ON tabela_esquerda.coluna = tabela_direita.coluna;
    ```

### INNER JOIN

- Retorna apenas os registros que têm correspondência nas duas tabelas.
    ```SQL
    SELECT * FROM tabela1 INNER JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
    ```

### UNION

- Combina o resultado de duas ou mais consultas em uma única lista de resultados, removendo duplicatas.
    ```SQL
    SELECT coluna1 FROM tabela1
    UNION
    SELECT coluna1 FROM tabela2;
    ```

### UNION ALL

- Combina o resultado de duas ou mais consultas em uma única lista de resultados, incluindo todas as linhas, mesmo que sejam duplicadas.
    ```SQL
    SELECT coluna1 FROM tabela1
    UNION ALL
    SELECT coluna1 FROM tabela2;
    ```
