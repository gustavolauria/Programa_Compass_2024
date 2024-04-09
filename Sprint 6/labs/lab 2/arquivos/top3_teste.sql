SELECT nome, SUM(total) AS total_utilizacoes
FROM meubanco.tb_nomes
WHERE ano >= 2010
GROUP BY nome
ORDER BY total_utilizacoes DESC
LIMIT 3