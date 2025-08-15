import socket

# 创建socket对象
socket_server = socket.socket()

# 绑定 ip 和 端口号
socket_server.bind(('localhost', 8888))

# 监听端口
# listen方法接受一个整数参数，表示接受的连接数量
socket_server.listen(1)

# 等待客户端连接，返回二元元组 (连接对象, 客户端的地址信息)
# conn 连接对象
# address 客户端的地址信息
# accept()是阻塞方法，如果没有连接，卡在这一行，不往下执行
conn, address = socket_server.accept()
print(f"接受到了客户端的连接，客户端的信息是:{address}")

while True:
    # 接受客户端信息
    # recv接受的参数是缓冲区大小，返回值是一个字节数组，不是字符串，可以通过decode方法转为字符串
    data = conn.recv(1024).decode('utf-8')
    print(f"客户端发来的消息是：{data}")

    # 发送回复消息，通过encode把字符串编码为字节数组
    msg = input("请输入回复的消息：")

    if(msg == '886'):
        break
    conn.send(msg.encode('utf-8'))


# 关闭连接
conn.close()
socket_server.close()