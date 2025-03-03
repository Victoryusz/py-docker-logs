# Monitoramento de Logs com Docker

Este projeto Dockeriza uma aplicação **Python** simples que gera logs fictícios com diferentes níveis (INFO, WARNING, ERROR, PERIGO), timestamps e contador crescente. A aplicação escreve os logs tanto no console quanto em um arquivo `app.log` dentro do container.

# Objetivo

Este laboratório ensina como containerizar uma aplicação Python, que gera logs fictícios (com níveis de log variados), e monitora esses logs no console e no arquivo de log.

## Funcionalidade:

- Geração contínua de logs com níveis variados (INFO, DEBUG, ERROR, PERIGO).
- Logs exibidos no console e salvos em um arquivo dentro do container.
- Contador incrementado a cada segundo.

## Como Usar:

1. **Construir a Imagem Docker:**

   ```bash
   docker build -t py-docker-logs .

   ```

2. **Executar o Container:**

   ```bash
   docker run -d --name py-docker-logs py-docker-logs

   ```

3. **Visualizar os Logs:**
   ```bash
   docker logs -f py-docker-logs
   ```

## CATEGORIAS:

- Monitoring
- Logging
- Python
