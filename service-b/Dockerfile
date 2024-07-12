# Dockerfile for service-b
FROM python:3.9-slim

WORKDIR /app

COPY service-b.py .

RUN pip install flask

EXPOSE 5001

CMD ["python", "service-b.py"]