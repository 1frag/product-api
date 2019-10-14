FROM python:3.7

RUN mkdir -p /src/backend
WORKDIR /src/backend

COPY requirements.txt /src/requirements.txt
RUN pip3 install -r /src/requirements.txt
RUN apt update -q
RUN apt install postgresql -y

COPY ./src /src/backend

EXPOSE 8000

CMD ["gunicorn", "--chdir", "backend", "--bind", ":8000", "backend.wsgi:application"]
