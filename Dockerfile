FROM tiangolo/uvicorn-gunicorn:python3.7

COPY . /

RUN pip install -r requirements.txt
