# STAGE 1: The "Tester" (This proves the code is usable)
FROM python:3.12-slim AS tester

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CRITICAL: This line satisfies the "Demonstrably Usable" requirement.
# If tests fail, the Docker build fails.
RUN python -m unittest discover tests

# STAGE 2: The "Final" (The clean, production-ready agent)
FROM python:3.12-slim

WORKDIR /app

# Copy only the installed packages from the tester stage (keeps it slim)
COPY --from=tester /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=tester /app .

# Default command to run your agent
CMD ["python", "chimera_brain.py"]