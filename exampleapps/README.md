### Example task producer and Celery app for testing your RabbitMQ cluster

This simple sample application will produce Celery tasks faster than it consumes them.
Use this to try things like stopping the master queue node to see how the Celery worker application responds.

#### Requirements   
You willl need memcached running if you want to use it as a results backend

#### Install
```
$virtualenv env
$. env/bin/activate
$pip install -r requirements.txt
```

#### To run the producer:
```
$python producer.py
```

#### To run the Celery worker application:
```
$celery -A consumer worker --loglevel=info --concurrency=1
```
