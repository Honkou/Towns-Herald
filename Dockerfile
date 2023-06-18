FROM python:3.9-alpine
COPY /requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY /source /app/
WORKDIR /app
CMD python main.py
