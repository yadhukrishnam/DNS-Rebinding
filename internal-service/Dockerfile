FROM python:3-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY src/. .

EXPOSE 7777

CMD ["python", "./app.py"]