FROM postgres:15

WORKDIR /usr/src/app

COPY ../../requirements.txt .

RUN pip install -r requirements.txt

COPY ../../src /app/src

CMD ["postgres"]