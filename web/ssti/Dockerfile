FROM python:3.9-slim

WORKDIR /app

COPY app/ /app/

RUN pip install --no-cache-dir -r requirements.txt

ENV FLAG=udctf{s3cur3_SSTI_3xp10it}

EXPOSE 5000

CMD ["python", "app.py"]
