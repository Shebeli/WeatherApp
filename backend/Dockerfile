FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE=false


WORKDIR /app

COPY . /app/

COPY poetry.lock pyproject.toml /app/

RUN pip install poetry
RUN poetry install --only main


EXPOSE 8000


RUN  python manage.py collectstatic --noinput

CMD gunicorn weatherproject.wsgi:application --bind 0.0.0.0:8000