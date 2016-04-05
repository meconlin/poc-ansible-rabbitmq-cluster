from celery import Celery
from time import sleep

# only consume from node0
BROKER = 'amqp://rabbitmqadmin:rabbitmqadmin@localhost:5673'
specialapp = Celery('consumer_special', broker=BROKER , backend="cache+memcached://localhost:11211" , include=['tasks'])

if __name__ == '__main__':
    specialapp.start()
