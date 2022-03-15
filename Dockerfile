FROM python:3.8-slim-buster
WORKDIR /ISP-2022-053502
COPY . .
CMD [ "python", "./task_1.py" ]
