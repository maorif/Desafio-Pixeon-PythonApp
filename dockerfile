FROM python:3.8

WORKDIR /app

COPY . /app

COPY ./requirements.txt /app
RUN pip install -r requirements.txt


EXPOSE 8080

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload", "--port=8080"]
