import threading
import time



t1 = threading.Semaphore()
t1.acquire()
t2 = threading.Semaphore()
t2.acquire()

room1 = 0
room2 = 0

def turnstile():
	t1.acquire()
	room2 += 1
	room1 -= 1
	print "0"
	if room1 == 0:
		print "0"
		t2.release()
	else:
		print "0"
		t1.release()
	t2.acquire()
	print "0"
	room2 -= 1

	print "this is the critcal section"
	time.sleep(1)
	if room2 == 0:
		print "0"
		t1.release()
	else:
		print "0"
		t2.release()

turn1 = threading.Thread(target=turnstile)
turn2 = threading.Thread(target=turnstile)
print "begin"
turn1.start()
turn2.start()
print "1"
turn1.join()
print "2"
turn2.join()


