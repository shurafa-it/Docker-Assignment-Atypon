FROM python:alpine3.10
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5003
COPY . /app
CMD ["python", "./app.py"] 

