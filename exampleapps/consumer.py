from celery import Celery
from time import sleep

app = Celery('consumer', include=['tasks'])

# import celery config file
app.config_from_object('celeryconfig')

if __name__ == '__main__':
    app.start()
