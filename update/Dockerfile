FROM python:3.7-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]