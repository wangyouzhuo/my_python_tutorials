import threading
import time
from queue  import Queue



def job(l,q):
    for i in range(len(l)):
        l[i] = l[i]**2
    q.put(l)



def multithreading():
    q = Queue() # 定义一个　队列

    threads_list = [] # 存放队列

    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]

    for i in range(4):
        t = threading.Thread(target=job , args=(data[i] , q))
        threads_list.append(t)
        t.start()
        t.join()

    # 保证　４　个线程　，　按照　１　２　３　４　的顺序执行完
    # for thread in threads_list:
    #     thread.join()

    results = []

    for _ in range(4):
        results.append(q.get())

    print(results)



if __name__ == "__main__":
    multithreading()

