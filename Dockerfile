FROM python:3.10.11

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN huggingface-cli download radlab/polish-qa-v2

CMD [ "python", "./app.py"]