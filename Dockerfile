FROM python:3.12

# Copy project files
COPY . /app

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose a default port (like 8080); this is optional and for documentation purposes only
EXPOSE 8080

# Run the app using gunicorn; $PORT must be set in the environment at runtime
CMD ["sh", "-c", "gunicorn --workers=4 --bind 0.0.0.0:${PORT:-8080} app:app"]