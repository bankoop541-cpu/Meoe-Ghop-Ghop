FROM --platform=linux/amd64 ubuntu:22.04

WORKDIR /app

# Install dependencies and make sure ping and other tools are available
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements and install them
COPY requirement.txt .
RUN pip3 install --no-cache-dir -r requirement.txt

# Copy all the remaining files
COPY . .

# Ensure the bgmi binary is executable
RUN chmod +x bgmi

# Run the watcher script
CMD ["python3", "watcher.py"]
