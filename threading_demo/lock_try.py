import threading


# 如果遇到这样的情况：　第一个线程执行完某个结果后，第二个线程才能开始执行，这个时候就需要锁ｌｏｃｋ

# 在job1临界区内　只有job1能够修改Ａ　，此时ｊｏｂ２无法接触Ａ所以一直阻塞
def job1():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=1
        print("job1" ,A)
    lock.release()


def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=10
        print("job2",A)
    lock.release()




if __name__ == "__main__":
    lock = threading.Lock()
    A  = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)

    t1.start()
    t2.start()
    # t1.join()
    # t2.join()


