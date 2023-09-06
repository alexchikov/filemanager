FROM ubuntu:22.04

RUN apt update && apt install -y python3.10

WORKDIR /manager

COPY src/exc.py exc.py
COPY src/main.py main.py

CMD ["python3.10", "main.py"]