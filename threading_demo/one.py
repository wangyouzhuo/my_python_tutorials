import threading
import time

def thread_job():
    print("T1 start \n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 stop \n")



def t2_job():
    print("T2 start")
    print("T2 stop")



def main():


    added_thread = threading.Thread(target=thread_job , name="T1")

    thread2 = threading.Thread(target=t2_job , name = 'T2')

    # 添加后　必须执行
    added_thread.start()

    thread2.start()

    # added_thread.join() 的含义是　阻塞added_thread　，added_thread完成后才执行接下来的程序
    thread2.join()

    #  已经激活的线程的数量
    print(threading.active_count())


    print("all done\n")




if __name__ == "__main__":
    main()