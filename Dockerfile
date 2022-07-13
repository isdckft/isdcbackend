FROM ubuntu:20.04
RUN apt-get update && apt-get install -y tzdata && apt install -y python3.8 python3-pip
RUN apt install python3-dev libpq-dev nginx -y
RUN pip install django gunicorn psycopg2
RUN pip install djangorestframework 
RUN pip install djangorestframework-simplejwt 
RUN pip install markdown 
RUN pip install django-filter
RUN pip install django-cors-headers
RUN pip install django-bootstrap4
RUN pip install pillow
RUN pip install dj-database-url
RUN pip install pandas
RUN pip install setuptools
RUN pip install sklearn
RUN pip install whitenoise

# COPY requirements.txt .
# RUN pip install -r requirements.txt

ADD . /app
WORKDIR /app
#RUN python manage.py migrate

EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "isdcbackend.wsgi"]
