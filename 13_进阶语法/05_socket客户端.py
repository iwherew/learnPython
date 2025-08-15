import socket

socker_client = socket.socket()
socker_client.connect(('localhost', 8888))

while True:
    msg = input("输入消息：")
    if msg == '886':
        break
    socker_client.send(msg.encode('utf-8'))
    data = socker_client.recv(1024).decode('utf-8')
    print(f"服务端回复的消息:{data}")

socker_client.close()