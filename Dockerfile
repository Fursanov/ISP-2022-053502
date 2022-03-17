FROM python:3.7.2-alpine3.8
WORKDIR /ISP-2022-053502
COPY . .
CMD [ "python", "./task_1" ]
