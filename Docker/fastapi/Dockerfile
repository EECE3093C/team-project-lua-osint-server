FROM python:3.10-alpine

WORKDIR /usr/app

COPY ../../requirements.txt .

RUN pip install -r requirements.txt

COPY ../../src/ ./src/

CMD ["python", "./src/main.py"]