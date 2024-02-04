#!/bin/bash

caminho="/home/gustavo/ecommerce/vendas/backup"

arquivo_final="relatorio_final.txt"

> "${arquivo_final}"

for arquivo in "${caminho}"/*.txt; do
    cat "${arquivo}" >> "${arquivo_final}"
done

echo "Arquivos unidos com sucesso!"

