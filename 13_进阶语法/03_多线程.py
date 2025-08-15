import time
import threading

def sing(msg, msg2):
    while True:
        print(f"sing:{msg}, msg2:{msg2}")
        time.sleep(1)

def dance(msg, msg2):
    while True:
        print(f"dance:{msg}, msg2:{msg2}")
        time.sleep(1)


# target: 执行函数
# kwargs: 字典入参
# args： 元组入参
if __name__ == '__main__':
    threading.Thread(target=sing, kwargs={"msg": "hello", "msg2": "hi"}).start()
    threading.Thread(target=dance, args=("world", "xixi",)).start()