from tasks import slow_add
from time import sleep
from random import randint

# What happens if primary queue node goes down while this is running

def load_it_up():
    """ produce a few right when we start up """
    for x in range(1, 10):
        result = slow_add.delay(randint(0,9),3)
        print "produced one task %s : "%result

def produce_forever():
    """ produce slow_add tasks forever, but dont be in a hurry to do it """
    while True:
        try:
            result = slow_add.delay(randint(0,9),3)
            sleeptime = randint(10,30)
            print "produced one task %s : then waiting : %s"%(result,sleeptime)
            sleep(sleeptime)
        except Exception as e:
            print "Error occured : %s"%e

load_it_up()
produce_forever()
