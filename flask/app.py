import os
from flask import Flask
from flask import url_for
from celery import Celery
from celery.result import AsyncResult
import celery.states as states

from celeryconfig import *

app = Flask(__name__)


celery_app = Celery('earning', broker=broker_url)

@app.route('/do_work/<int:param1>')
def do_work(param1):
    task0 = celery_app.send_task('earning.add', queue='earning', args=[param1], kwargs={})
    
    return "<a href='{url}'>check status of {id} </a> <br/>".format(
        id = task0.id,
        url = url_for('check_task', id=task0.id, _external=True)
    )

@app.route('/check/<string:id>')
def check_task(id):
    res = AsyncResult(id)
    if res.state==states.PENDING:
        return res.state
    else:
        return str(res.result)

if __name__ == '__main__':
    app.run(
        debug = True,
        port = int(5000),
        host = '0.0.0.0',
    )
