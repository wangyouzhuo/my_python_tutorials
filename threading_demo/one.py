import threading

def thread_job():
    print("This is an added_thread,number is %s"% threading.current_thread())





def main():

    # 注意　如果此处写为　target=thread_job()  那么无论执行与否　线程都会执行
    # 创建线程　同时　输入target 是线程要做的事情
    added_thread = threading.Thread(target=thread_job)

    # 添加后　必须执行
    added_thread.start()

    # 已经激活的线程的数量
    print(threading.active_count())

    # 查看已经激活的线程的信息
    print(threading.enumerate())

    # 查询当前运行的程序的线程
    print(threading.current_thread())



if __name__ == "__main__":
    main()