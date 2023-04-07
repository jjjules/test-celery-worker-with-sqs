FROM python:alpine


RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev curl-dev
    

# Install the required packages - celery[s3]
RUN pip install --upgrade pip
RUN pip install celery[sqs] celery-s3 boto3 pycurl


# copy source code
COPY . /earning
WORKDIR /earning


# To start the celery worker service: --config=celeryconfig
ENTRYPOINT celery -A earning worker -Q earning

