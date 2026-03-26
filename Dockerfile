FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app/library

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
