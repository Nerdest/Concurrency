#prodcon.py

import threading
import Queue
from random import randint
import time


q = Queue.Queue(0);

def prod():
	while 1:
		rand = randint(1,100000)
		q.put(rand)
		print str(rand) + " was added to queue\n"
		time.sleep(1)
def con1():
	time.sleep(3)
	while 1:
		print str(q.get()) + " was removed from queue by consumer 1\n"
		time.sleep(randint(1,3))

def con2():
	time.sleep(3)
	while 1:
		print str(q.get()) + " was removed from queue by consumer 2\n"
		time.sleep(randint(1,3))

prod = threading.Thread(target=prod)
con1 = threading.Thread(target=con1)
con2 = threading.Thread(target=con2)
prod.start()
con1.start()
con2.start()
prod.join()
con1.join()
con2.join()