FROM python:3.13-alpine

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY ./app ./app

# Expose port
EXPOSE 3000

# Run the app with Uvicorn, bind to 0.0.0.0 and port 3000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000", "--workers", "4", "--no-access-log", "--no-server-header"]