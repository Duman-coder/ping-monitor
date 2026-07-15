FROM python:3.11-slim

# устанавливаем ping (пакет iputils-ping)
RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ping_check.py .
COPY hosts.txt .

CMD ["python3", "ping_check.py"]
