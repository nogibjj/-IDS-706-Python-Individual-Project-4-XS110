FROM python:3.11

WORKDIR /

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:asgi_app", "--host", "0.0.0.0", "--port" , "8000"]
