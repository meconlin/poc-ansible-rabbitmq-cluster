from celery import Celery
from time import sleep

app = Celery('consumer', include=['tasks'])
