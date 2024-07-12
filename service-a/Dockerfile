# Dockerfile for service-a
FROM python:3.9-slim

WORKDIR /app

COPY service-a.py .
COPY templates /app/templates

RUN pip install flask requests

EXPOSE 5000

CMD ["python", "service-a.py"]
