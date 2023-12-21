FROM python:3.12

WORKDIR /app

COPY poetry.lock pyproject.toml /app/
RUN pip install poetry && poetry install

COPY . /app/

EXPOSE 8000

CMD ['poetry', "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]