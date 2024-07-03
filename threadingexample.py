import threading
import time


def thread_function(name):
    print(name)
    time.sleep(2)
    print(name)

for i in range(1,4):
    x = threading.Thread(target=thread_function, args=('omar'+str(i),))
    x.start()
