import threading
import time


def sequence(n):
    for i in range(n):
        print(i**2)
        time.sleep(1)

'''start_time=time.time()
sequence(5)
sequence(7)
end_time=time.time()
run_time=end_time-start_time
print(run_time)'''#this is without using threads run time 12.9579473677 seconds 


#by using threads we can execute concurrently
start_time=time.time()
t1=threading.Thread(target=sequence,args=(10,))
t2=threading.Thread(target=sequence,args=(7,))
t1.start()
t2.start()

t1.join()
t2.join()
end_time=time.time()
run_time=end_time-start_time
print(run_time) # run time 10.857867 seconds
