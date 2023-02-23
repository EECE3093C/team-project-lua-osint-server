FROM python:3.10-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./src /app/src

CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0"]