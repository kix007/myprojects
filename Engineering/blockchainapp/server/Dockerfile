# Install packages
FROM python:3.8-alpine as packages

RUN apk add g++ libc-dev libffi-dev 
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo
RUN pip install pipenv

WORKDIR /pipfile
COPY Pipfile ./

ENV PIP_USER=1
ENV PIP_IGNORE_INSTALLED=1
ENV PYROOT /pyroot
ENV PYTHONUSERBASE $PYROOT

RUN pip install --upgrade pip
RUN pipenv install --system --deploy --skip-lock

# Build
FROM python:3.8-alpine

ENV PYTHONUNBUFFERED=1
ENV TZ=Africa/Johannesburg

RUN apk add tzdata
WORKDIR /app
COPY --from=packages /pyroot/ /usr/local/
COPY . .
EXPOSE 8001

CMD ["python", "main.py"]