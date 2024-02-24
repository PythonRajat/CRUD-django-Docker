FROM python:3-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /crudproj
#COPY requirements.txt /code/
COPY . /crudproj/
RUN pip install -r requirements.txt