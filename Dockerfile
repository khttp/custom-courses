FROM python:3.9-slim as build

WORKDIR /usr/local/app

copy requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

copy . .

EXPOSE 8000

CMD ["python", "src/main.py"]

# Stage 2: Production
FROM python:3.9-slim

WORKDIR /usr/local/app

# Copy only the necessary files from the build stage
COPY --from=build /usr/local/app /usr/local/app

copy requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "src/main.py"]
