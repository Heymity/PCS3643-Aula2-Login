# Dockerfile para PostgreSQL

# Utiliza a imagem oficial do PostgreSQL
FROM postgres:15

# Define as variáveis de ambiente para o banco de dados
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=1234
ENV POSTGRES_DB=api_db

# Expõe a porta padrão do PostgreSQL
EXPOSE 5432

# Opcional: Copie scripts de inicialização para o diretório de inicialização do PostgreSQL
# COPY ./init.sql /docker-entrypoint-initdb.d/untu