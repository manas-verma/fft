FROM rust:1.61.0

# Install dependencies
COPY ./requirements.txt /tmp/requirements.txt
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install -r /tmp/requirements.txt

# Copy source code
COPY ./src /app
WORKDIR /app

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]

EXPOSE 8000
