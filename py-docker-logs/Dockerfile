# Usa uma imagem python oficial como base
FROM python:3.9-slim 

# Copia o cídigo da aplicação para dentro do container
COPY app.py /app.py 

# Define o diretório de trabalho
WORKDIR /

# Comando para rodar aplicação Python
CMD ["python", "app.py"]