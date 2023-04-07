import os
import sys
import time
import random
import logging
from celery import Celery
from celery.exceptions import MaxRetriesExceededError
# from billiard import current_process

app = Celery('earning')
default_config = 'celeryconfig'
app.config_from_object(default_config)

@app.task(name='earning.add', bind=True, max_retries=3)
def add(self, x):
    try:
        timestamp = time.time()
        print(str(self.request.retries) + ", earning -> " + str(timestamp) + ", " + str(x))
        return f"AAA -> {x}"
    except Exception as e:
        logging.error(e, exc_info=True)
        
        exc_type, exc_obj, exc_tb = sys.exc_info()
        
        error = exc_type
        message = str(e)
        line_number = exc_tb.tb_lineno
        filename = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    
        try:
            self.retry(countdown=int(random.uniform(2, 4) ** self.request.retries))
        except MaxRetriesExceededError as me:
            logging.error(me, exc_info=True)
            print(f"ERROR:\n{error}\n{message}\n{filename}\n{line_number}")
            print()
            print()
            raise e


