FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
COPY . /app/server
WORKDIR /app/server

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
