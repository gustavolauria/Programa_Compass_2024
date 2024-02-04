# Resumo Git 

### git add:

- Adiciona alterações ao stage (área de preparação para commit).
    Adicionar um arquivo específico: git add nome_do_arquivo.
    Adicionar todos os arquivos modificados: git add ..

### git archive:

- Cria um arquivo zip, tar ou outro formato a partir de uma árvore de trabalho do Git.
    Criar um arquivo zip de um commit específico: git archive -o arquivo.zip HEAD.

### git branch:

- Lista, cria ou exclui branches.
    Criar uma nova branch: git branch nome_da_ramificacao.
    Listar branches: git branch.
    Excluir uma branch: git branch -d nome_da_ramificacao.

### git checkout:

- Muda entre branches ou restaura arquivos do diretório de trabalho.
    Mudar para uma branch existente: git checkout nome_da_ramificacao.
    Criar e mudar para uma nova branch: git checkout -b nova_ramificacao.

### git clone:

- Clona um repositório existente para um novo diretório local.
    git clone URL_do_repositorio.

### git commit:

- Registra as alterações no repositório como um novo commit.
    git commit -m "Mensagem do commit".

### git diff:

- Mostra as diferenças entre alterações no diretório de trabalho e no índice (staged) ou entre commits.
    Diferenças entre o diretório de trabalho e o índice: git diff.
    Diferenças entre commits: git diff commit_A commit_B.

### git fetch:

- Busca as alterações do repositório remoto, mas não mescla automaticamente no branch local.
    git fetch origin.

### git init:

- Inicia um novo repositório Git local.
    git init.

### git log:

- Mostra o histórico de commits.
    git log.

### git merge:

- Une branches no repositório.
    git merge nome_da_ramificacao.

### git mv:

- Move ou renomeia arquivos ou diretórios e registra as mudanças no repositório.
    git mv nome_antigo nome_novo.

### git pull:

- Atualiza o repositório local com as alterações do repositório remoto.
    git pull origin nome_da_ramificacao.

### git push:

- Envia commits locais para um repositório remoto.
    git push origin nome_da_ramificacao.

### git remote:

- Mostra informações sobre repositórios remotos conectados ao repositório local.
    Listar repositórios remotos: git remote -v.
    Adicionar um novo repositório remoto: git remote add nome_remoto URL_do_repositorio.

### git reset:

- Desfaz alterações no histórico de commits.
    Desfazer commits mantendo alterações no diretório de trabalho: git reset HEAD~1.
    Desfazer commits e descartar todas as alterações: git reset --hard HEAD~1.

### git rm:

- Remove arquivos do diretório de trabalho e os marca para remoção no próximo commit.
    git rm nome_do_arquivo.

### git stash:

- Armazena temporariamente alterações não commitadas.
    Armazenar alterações: git stash.
    Recuperar alterações armazenadas: git stash apply.

### git status:

- Mostra o estado das alterações no diretório de trabalho em relação ao repositório.
    git status.

### git show:

- Exibe informações detalhadas sobre um objeto específico (como commit, tag ou árvore).
    git show SHA_do_commit.

### git tag:

- Cria uma tag para marcar um ponto específico na história do repositório.
    git tag -a nome_da_tag -m "Mensagem descritiva".