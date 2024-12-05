FROM python:3.9-slim 
 
# Устанавливаем рабочую директорию 
WORKDIR /app 
 
# Копируем все файлы в контейнер 
COPY . /app/ 
 
# Устанавливаем зависимости 
RUN pip install --no-cache-dir -r requirements.txt 
 
# Устанавливаем переменные окружения для Django 
ENV PYTHONUNBUFFERED 1 
 
# Открываем порт для Django (по умолчанию 8000) 
EXPOSE $PORT 
 
# Запускаем сервер Django 
CMD python manage.py runserver 0.0.0.0:$PORT
