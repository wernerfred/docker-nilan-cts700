FROM python:3.9-alpine as base

FROM base as builder

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir --prefix=/app -r requirements.txt

FROM base

COPY --from=builder /app /usr/local

COPY ./app /app 

EXPOSE 8080

CMD [ "python", "/app/prom_export.py" ] 