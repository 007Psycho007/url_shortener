FROM python:3.9-slim

WORKDIR /app

COPY application/ .
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 5000

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production  

CMD ["python", "run.py"]
