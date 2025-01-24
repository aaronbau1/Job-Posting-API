FROM python:3.9-slim
WORKDIR /app

# Copy dependencies
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code into container
COPY . /app/

# Expose port
EXPOSE 8000

# FastAPI Uvicorn startup command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
