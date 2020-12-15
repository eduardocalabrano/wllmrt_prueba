# imagen python
FROM python:3.8-alpine

# definir ruta de trabajo
WORKDIR /app

# variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# archivo requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copiar proyecto
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser -D myuser
USER myuser

# gunicorn
CMD gunicorn desafio_wallmart.wsgi:application --bind 0.0.0.0:$PORT
