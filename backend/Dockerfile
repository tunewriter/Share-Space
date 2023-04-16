#
FROM python:3.10

# Set the working directory
WORKDIR /code

# Upgrade pip and install required packages
RUN pip install --upgrade pip
RUN pip3 install uvicorn fastapi supabase pytest python-dotenv

# Copy the application code
COPY ./app /code/app

# Copy the SSL certificate and key files from the local 'certs' directory
COPY ./certs /certs

# Start Uvicorn with SSL support
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "443", "--ssl-keyfile", "/certs/privkey.pem", "--ssl-certfile", "/certs/fullchain.pem"]

# If you don't have an SSL certificate, you can use the following command instead:
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
