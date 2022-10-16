FROM python:3.10

WORKDIR /app
RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .
RUN mkdir logs
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
