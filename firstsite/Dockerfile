FROM python:3.10

# Встановлюємо робочу директорію всередині контейнера
WORKDIR /firstsite

# Копіюємо файли проєкту в контейнер
COPY . /firstsite

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Виконуємо міграції
RUN python manage.py migrate

# Відкриваємо порт 8000
EXPOSE 8000

# Запускаємо Django-сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]