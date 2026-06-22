import threading
import time

def f():
    print("Hi Hi")
    time.sleep(2)
    print("Hello")
    
def f1():
    print("welcome")
    time.sleep(1)
    print("Bye Bye")
    
t1 = threading.Thread(target=f)
t2 = threading.Thread(target=f1)

t1.start()
t2.start()
t2.join()
t2.join()
print("Done.....")