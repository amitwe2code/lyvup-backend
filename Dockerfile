
FROM python:3.12-slim

WORKDIR /backend

COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN  pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
