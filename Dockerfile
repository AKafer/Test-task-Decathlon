FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY todolist/ /app

RUN chmod a+x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

CMD ["python3", "manage.py", "runserver", "0:8000"]