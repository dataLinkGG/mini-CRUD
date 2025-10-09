FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY gunicorn.py ./

RUN mkdir -p /logs

ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.main:app

EXPOSE 8000

CMD ["gunicorn", "-c", "gunicorn.py", "app.main:app"]
