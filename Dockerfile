FROM python:3.12

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["sh", "-c", "python app/manage.py migrate && python app/manage.py create_superuser && python app/manage.py runserver 0.0.0.0:8000"]
