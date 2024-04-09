WITH top_nomes AS (
	SELECT nome,
		FLOOR(ano / 10) * 10 AS decada,
		SUM(total) AS total_por_decada,
		ROW_NUMBER() OVER (
			PARTITION BY FLOOR(ano / 10) * 10
			ORDER BY SUM(total) DESC
		) AS rank
	FROM meubanco.tb_nomes
	WHERE ano >= 1950
	GROUP BY nome,
		FLOOR(ano / 10) * 10
)
SELECT nome,
	decada,
	total_por_decada
FROM top_nomes
WHERE rank <= 3
ORDER BY decada ASC,
	rank ASC