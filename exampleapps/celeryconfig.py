from kombu import Exchange, Queue

CELERY_DEFAULT_QUEUE = 'test-ha-queue'
CELERY_QUEUES = (
    Queue('test-ha-queue', Exchange('test-ha-queue'), routing_key='test-ha-queue'),
)

USER = 'rabbitmqadmin'
PASSWD = 'rabbitmqadmin'
HOST = 'localhost'

# watch that your ports here line up with the exported ports from your vagrant or AWS configuration
CELERY_RESULT_BACKEND = "cache+memcached://%s:11211"%HOST
BROKER_URL = ["amqp://%s:%s@%s:5673"%(USER,PASSWD,HOST),
              "amqp://%s:%s@%s:5674"%(USER,PASSWD,HOST),
              "amqp://%s:%s@%s:5775"%(USER,PASSWD,HOST)
              ]
