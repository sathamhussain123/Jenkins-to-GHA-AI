FROM python:3.11-slim

WORKDIR /app

COPY app/ /app/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & python file_watcher.py"]

//CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
