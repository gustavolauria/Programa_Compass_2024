# Resumo Linux

### cd (Change Directory):

- Serve para mudar de diretórios.
    cd -: Voltar para o diretório anterior.
    cd ~: Mover para a home do usuário atual.

### ls (List):

- Exibe o conteúdo do diretório atual.
    ls -l: Lista detalhada.
    ls -a: Mostra arquivos ocultos.
    ls -h: Torna o tamanho dos arquivos mais legível.

### clear:

- Limpa a tela do terminal, removendo o histórico de comandos anteriores.

### cat (Concatenate):

- Exibe o conteúdo de arquivos de texto.
    Pode ser usado para concatenar e exibir múltiplos arquivos: cat file1.txt file2.txt.

### touch:

- Cria arquivos vazios ou atualiza o carimbo de data/hora de arquivos existentes.

### man (Manual):

- Abre o manual online para um comando específico.
    man ls exibirá o manual para o comando 'ls'.
    Use as setas para rolar, 'q' para sair.

### mkdir (Make Directory):

- Cria um novo diretório.
    mkdir nome_do_diretorio.

### rm (Remove):

- Remove arquivos ou diretórios, use com cuidado, pois a remoção é irreversível.
    rm arquivo.txt ou rm -r diretorio.

### rmdir (Remove Directory):

- Remove diretórios vazios.
    rmdir nome_do_diretorio.

### cp (Copy):

- Copia arquivos ou diretórios.
    cp arquivo.txt destino/ ou cp -r diretorio/ destino/ (para cópia recursiva).

### mv (Move):

- Move ou renomeia arquivos e diretórios.
    mv arquivo.txt novo_nome.txt ou mv arquivo.txt diretorio_destino/.

### apt-get:

- Utilizado para gerenciar pacotes.
    Instalação de pacotes: sudo apt-get install nome_do_pacote.
    Atualização do sistema: sudo apt-get update && sudo apt-get upgrade.

### head:

- Exibe as primeiras linhas de um arquivo de texto.
    head -n 10 arquivo.txt (mostra as primeiras 10 linhas).

### tail:

- Exibe as últimas linhas de um arquivo de texto.
    tail -n 20 arquivo.txt (mostra as últimas 20 linhas).

### grep:

- Filtra linhas de texto que correspondem a um padrão.
    grep "palavra" arquivo.txt.

### find:

- Procura arquivos ou diretórios em uma hierarquia.
    find /caminho -name "nome_arquivo".

### locate:

- Localiza rapidamente a localização de arquivos no sistema.
    locate nome_arquivo.

## Nano:
Abrir um arquivo: nano nome_do_arquivo
Salvar alterações: Pressione Ctrl + O, depois pressione Enter.
Sair do Nano: Pressione Ctrl + X.
Desfazer: Alt + U.
Refazer: Alt + E.

## Vim:
Abrir um arquivo: vim nome_do_arquivo.
Modo de Inserção: Pressione i para entrar no modo de inserção (para começar a digitar).
Salvar e Sair: No modo de comando, digite :w para salvar e :q para sair.
Para salvar e sair ao mesmo tempo, use :wq.
Sair sem Salvar: No modo de comando, digite :q! para sair sem salvar alterações.
Desfazer: No modo de comando, pressione u.
Refazer: No modo de comando, pressione Ctrl + r.
