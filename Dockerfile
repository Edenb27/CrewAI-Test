FROM python:3.10-alpine
WORKDIR /usr/src/app
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY . .

CMD ["python3", "main.py"]