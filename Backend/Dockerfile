FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org Flask==1.1.2 Jinja2==2.11.3

RUN pip install --upgrade jinja2

RUN pip install --upgrade flask

RUN pip install flask_cors

EXPOSE 5000

CMD ["python", "app.py"]
