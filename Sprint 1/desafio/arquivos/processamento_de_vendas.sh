#!/bin/bash

caminho="/home/gustavo/ecommerce"

mkdir -p vendas

cp ${caminho}/dados_de_vendas_fix.csv ${caminho}/vendas/

mkdir -p ${caminho}/vendas/backup

data_formato=$(date +%Y%m%d)

cp ${caminho}/vendas/dados_de_vendas_fix.csv ${caminho}/vendas/backup/dados-${data_formato}.csv

mv ${caminho}/vendas/backup/dados-${data_formato}.csv ${caminho}/vendas/backup/backup-dados-${data_formato}.csv
 
data_hora=$(date +"%Y/%m/%d %H:%M")

ultimos_10_1=$(sed -n '2s/.*\(.\{10\}\)$/\1/p' ${caminho}/vendas/backup/backup-dados-${data_formato}.csv)
ultimos_10=$(tail -n 1 ${caminho}/vendas/backup/backup-dados-${data_formato}.csv |rev| cut -c -10|rev)
total=$(($(wc -l < ${caminho}/vendas/backup/backup-dados-${data_formato}.csv) - 1))
linhas=$(head -n 10 ${caminho}/vendas/backup/backup-dados-${data_formato}.csv)

echo "Data: ${data_hora}" > ${caminho}/vendas/backup/relatorio-${data_formato}.txt
echo "Primeiro registro: ${ultimos_10_1}" >> ${caminho}/vendas/backup/relatorio-${data_formato}.txt
echo "Ultimo registro: ${ultimos_10}" >> ${caminho}/vendas/backup/relatorio-${data_formato}.txt
echo "Total de itens: ${total}" >> ${caminho}/vendas/backup/relatorio-${data_formato}.txt
echo "Head: ${linhas}" >> ${caminho}/vendas/backup/relatorio-${data_formato}.txt

zip -r ${caminho}/vendas/backup/backup-dados-${data_formato}.zip ${caminho}/vendas/backup/backup-dados-${data_formato}.csv

rm ${caminho}/vendas/backup/backup-dados-${data_formato}.csv
rm ${caminho}/vendas/dados_de_vendas_fix.csv 

echo "Script executado com sucesso!"

