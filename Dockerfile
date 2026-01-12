FROM python:3.13.11-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY . /app
WORKDIR /app
RUN uv sync --locked

ENV PYTHONPATH=/app
ENV DEBUG=True
ENV DJANGO_SETTINGS_MODULE=minitrello.settings
ENV DJANGO_WATCHFILES_FORCE_POLLING=true

RUN uv run manage.py migrate
EXPOSE 8000
CMD [ "uv","run","gunicorn", "-b 0.0.0.0:8000", "minitrello.wsgi" ]
