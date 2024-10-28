# Используйте официальный образ Python
FROM python:3.13

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файлы проекта в контейнер
COPY . .

# Установите зависимости
RUN pip install -r requirements.txt
RUN pip install --upgrade Flask Werkzeug


# Создайте директорию storage, если её нет
RUN mkdir -p storage

# Команда для запуска приложения
CMD ["python", "main.py"]



