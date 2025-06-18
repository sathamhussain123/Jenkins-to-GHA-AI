FROM python:3.11-slim

WORKDIR /app

# ✅ Add git (critical!)
RUN apt-get update && apt-get install -y git && apt-get clean

COPY app/ /app/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
