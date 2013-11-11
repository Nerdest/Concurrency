#readwrite.py

from random import choice
from random import randint
import time
import threading


master = ["this","is","an","amazing","sentence"]
adjectives =["defeated","defiant","delicious","delightful","depressed","determined","dirty","disgusted","disturbed","dizzy","dry","dull","dusty","eager","early","elated","embarrassed","empty","encouraging","energetic","enthusiastic","envious","evil","excited","exuberant","faint","fair","faithful","fantastic","fast","fat","few","fierce","filthy","fine","flaky","flat","fluffy","foolish","frail","frantic","fresh","friendly","frightened","funny","fuzzy","gentle","giant","gigantic","good"]

def write():
	while 1:	
		master[3] = choice(adjectives)
		print "The all powerful writer declares that the sentence is now " + str(master[3])
		time.sleep(1)


def reader(id):
	while 1:
		sen = " ".join(master)
		print "reader " + str(id) + " thinks " + str(sen)
		time.sleep(randint(1,3))

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



