FROM python:3.11-slim

WORKDIR /app

# System libraries required by OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install CPU-only PyTorch
RUN pip install --no-cache-dir \
    torch==2.14.0+cpu \
    torchvision==0.29.0+cpu \
    --index-url https://download.pytorch.org/whl/cpu

# Install RetinaAI dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]