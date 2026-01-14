FROM python:3.13.11-slim-trixie
ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED = 1
WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev 

COPY ./ ./
EXPOSE 8080

CMD [ "uv", "run" ,"manage.py","runserver","0.0.0.0:8080" ]










# COPY . /app
# RUN uv sync --locked

# ENV PYTHONPATH=/app
# ENV DEBUG=True
# ENV DJANGO_SETTINGS_MODULE=minitrello.settings
# ENV DJANGO_WATCHFILES_FORCE_POLLING=true

# RUN uv run manage.py migrate
# EXPOSE 8000
# CMD [ "uv","run","gunicorn", "-b 0.0.0.0:8000", "minitrello.wsgi" ]
