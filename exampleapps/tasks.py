from celery.decorators import task
from time import sleep
from consumer import app

@app.task
def slow_add(x, y, sleeptime=60):
    """ I slowly add numbers together """
    sleep(sleeptime)
    return x + y
