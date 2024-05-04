# Python 3.9 tabanlı resmi Docker imajını kullan
FROM python:3.9-slim

# Çalışma dizinini /app olarak belirt
WORKDIR /app

# API kodunu kopyala
COPY . /app

# Gerekli Python paketlerini yükle
RUN pip install --no-cache-dir -r requirements.txt

# Flask uygulamasını çalıştır
CMD ["python", "main.py"]
