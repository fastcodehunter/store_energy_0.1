FROM python:3.12

WORKDIR /store

COPY .. /store/

RUN pip install -r requirements.txt

CMD [ "python", "./manage.py", "runserver" ]