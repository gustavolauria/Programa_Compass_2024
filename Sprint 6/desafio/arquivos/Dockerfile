FROM python:3

WORKDIR /app

COPY carregar.py .
COPY movies.csv .
COPY series.csv .

RUN pip install boto3

CMD ["python", "carregar.py"]