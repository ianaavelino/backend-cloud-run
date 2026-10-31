# Imagem oficial do Python
FROM python:3.14-slim

# Configurações do Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho
WORKDIR /app

# Instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o projeto
COPY . .

# Reúne os arquivos estáticos para produção
RUN SECRET_KEY=build-only-placeholder DEBUG=False \
    python manage.py collectstatic --noinput

# Porta utilizada pelo Cloud Run
ENV PORT=8080
EXPOSE 8080

# Inicializa a aplicação com Gunicorn
CMD ["sh", "-c", "gunicorn config.wsgi:application --bind 0.0.0.0:${PORT}"]