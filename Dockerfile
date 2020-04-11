FROM python:3.8-buster

RUN mkdir -p /app
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY zakat /app/zakat

EXPOSE 8000

VOLUME [ "/app/zakat/media" ]

CMD [ "python", "zakat/manage.py", "runserver", "0.0.0.0:8000" ]
