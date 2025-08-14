FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN apt-get update && apt-get install -y curl
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app ./app
COPY ./main.py ./main.py
COPY ./worker ./worker
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
