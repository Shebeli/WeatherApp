FROM python:3.12

WORKDIR /app

COPY poetry.lock pyproject.toml /app/


RUN pip install poetry
RUN poetry install

COPY . /app/

EXPOSE 8000


CMD ["sh", "-c", "poetry run python manage.py makemigrations && poetry run python manage.py migrate && poetry run python manage.py runserver 0.0.0.0:8000"]