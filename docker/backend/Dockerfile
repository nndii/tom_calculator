FROM python:3.9.6-buster

ENV POETRY_VERSION=1.1.7 \
    POETRY_VIRTUALENVS_CREATE=false

RUN pip3 install "poetry==$POETRY_VERSION"

WORKDIR /app/

COPY backend/poetry.lock backend/pyproject.toml ./
RUN poetry install --no-interaction --no-ansi --no-dev

COPY backend/ ./

EXPOSE 8000

CMD ["gunicorn", "tom_calculator.app:app", "--bind", "0.0.0.0:8000", "--worker-class", "aiohttp.worker.GunicornUVLoopWebWorker"]