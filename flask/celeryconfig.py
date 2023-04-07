import os
from kombu.utils.url import safequote

aws_access_key_id = safequote(os.environ.get('AWS_ACCESS_KEY_ID'))
aws_secret_access_key = safequote(os.environ.get('AWS_SECRET_ACCESS_KEY'))


## Broker settings.
broker_url = f"sqs://{aws_access_key_id}:{aws_secret_access_key}@"
broker_transport_options = {
    'region': 'eu-central-1',
    # 'queue_name_prefix': 'qgen-jobs-from-backend-',
    # 'predefined_queues': {
    #     'earning': {
    #         'url': 'https://sqs.eu-central-1.amazonaws.com/026768510714/new-queue-for-celery',
    #         'access_key_id': os.environ.get('AWS_ACCESS_KEY_ID'),
    #         'secret_access_key': os.environ.get('AWS_SECRET_ACCESS_KEY'),
    #     }
    # }
}


## Using the database to store task state and results.
result_backend = 'celery_s3.backends.S3Backend'
CELERY_S3_BACKEND_SETTINGS = {
    'aws_access_key_id': os.environ.get('AWS_ACCESS_KEY_ID'),
    'aws_secret_access_key': os.environ.get('AWS_SECRET_ACCESS_KEY'),
    'bucket': 'test-celery-worker',
    'aws_region': 'eu-central-1',
}
result_persistent = True
