# PCS3643-Aula2-Login
Exercício de Laboratório de Engenharia de Software que visa criar um sistema de login com FastAPI

1. Instalar o UV
2. Instalar o Docker
3. Ter instalado o Node e npm em versão recente

## Criar container do Postgres

Executar na pasta root do projeto

```sh
docker run --name postgressql -e POSTGRES_PASSWORD=1234 -p 5432:5432 -d postgres
```

Se houve sucesso, o banco pode ser acessado em localhost, usuario postgres, senha 1234, porta 5432.

## Setup do Projeto

Primeiramente cerifique que o gerenciador uv está baixado. Entre na pasta API:

```sh
cd API
```

Baixe as dependências do projeto:

```sh
uv sync
```

Agora vamos configuarar o banco de dados caso esse ainda não tenha sido criado/configurado. Executar o seguinte comando

```sh
uv run .\templates\create_db.py
```

E executamos a migração:

```sh
uv run alembic upgrade head
```

Uma observação: Se a pasta alembic por algum motivo não existir, deve-se primeiro executar
Com sucesso, caso o Alembic não esteja inicializado (ou seja a pasta não exista) executar:

```sh
uv run alembic init alembic
cp -f templates/env.py alembic/env.py 
```

Caso o comando cp dê erro, apenas delete o arquivo alembic/env.py e o substitua manualmente pelo templates/env.py

Caso queira mudar o banco de dados deve-se modificar o arquivo de models e então criar uma revisão e dar upgrade:

```sh
alembic revision --autogenerate -m "Criando Tabela Users"
uv run alembic upgrade head
```

# Rodando a API

Primeiramente conferir que o docker com postgres está executando e então, **dentro da pasta API**, executar:

```sh
uv run fastapi dev
```

# Rotando o Front

**Dentro da pasta Frontend** execute para baixar as dependencias:

```sh
npm i
```

E então execute

```sh
npx vite
```



