FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry==1.8.5 --no-cache-dir

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --only main

COPY . .

EXPOSE 5000

CMD ["poetry", "run", "python", "app.py"]
