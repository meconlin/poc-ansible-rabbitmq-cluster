from celery import Celery
from time import sleep
from kombu import Exchange, Queue

# only consume from single node, not multi node connection
#

#BROKER = 'amqp://rabbitmqadmin:rabbitmqadmin@localhost:5673'
BROKER = 'amqp://rabbitmqadmin:rabbitmqadmin@ip-192-168-16-154.vpc.team.getgoing.com:5672'
specialapp = Celery('consumer_special', broker=BROKER , backend="cache+memcached://localhost:11211" , include=['tasks'] )
specialapp.conf.update(
    CELERY_DEFAULT_QUEUE = 'test-ha-queue',
    CELERY_QUEUES = ( Queue('test-ha-queue', Exchange('test-ha-queue'), routing_key='test-ha-queue'), )
)

if __name__ == '__main__':
    specialapp.start()
