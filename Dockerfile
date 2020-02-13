FROM python:3.7.6-stretch

RUN pip install django

RUN mkdir django

WORKDIR /django

EXPOSE 8000

COPY . .

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]

