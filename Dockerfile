# Используем официальный образ Python
FROM python:3.9

# Устанавливаем рабочую директорию в контейнере
WORKDIR /Back

# Копируем файл с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в рабочую директорию контейнера
COPY . .

# Открываем порт для доступа к FastAPI
EXPOSE 8000

# Запускаем приложение FastAPI
CMD ["uvicorn", "Back.main:app", "--host", "0.0.0.0", "--port", "8000"]
