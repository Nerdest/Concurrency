#readwrite.py

from random import randint
import time
import threading


master = [0,1]
count = 0
def write():
	for x in xrange(1,10):
		sema.acquire()
		print "The first value of the array before writing is " + str(master[0])
		master[0] += 1
		print "The second value of the array before writing is " + str(master[1])
		master[1] +=1
		x+=1
		sema.release()
		time.sleep(1)


def reader(id):
	global count
	for x in xrange(1,10):
		if( count<1):
			sema.acquire()
		count +=1
		print "reader " + str(id) + " sees " + str(master[0]) + " as the first value of the array\n"
		print "reader " + str(id) + " sees " + str(master[1]) + " as the second value of the array\n"
		
		x+=1
		count -=1
		if(count<1):
			sema.release()
		time.sleep(2)


sema = threading.Semaphore()
writer = threading.Thread(target=write)
reader1 = threading.Thread(target=reader, args=(1,));
reader2 = threading.Thread(target=reader, args=(2,));
reader3 = threading.Thread(target=reader, args=(3,));
reader4 = threading.Thread(target=reader, args=(4,));

writer.start()
reader1.start()
reader2.start()
reader3.start()
reader4.start()
writer.join()
reader1.join()
reader2.join()
reader3.join()
reader4.join()



