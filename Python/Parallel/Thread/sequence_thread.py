import threading
from time import ctime,sleep

def function(i):
    sleep(1)
    print ("function called by thread %i\n"  %i)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=function , args=(i,))
    threads.append(t)
    t.start()
    t.join()



