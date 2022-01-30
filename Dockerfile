FROM python:3.8

WORKDIR /app
COPY . /app

RUN pip3 install poetry
RUN poetry install

CMD ["poetry","run", "python3", "./pda/main.py"]