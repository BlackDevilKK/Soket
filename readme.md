# TCP编程

![python](https://img.shields.io/badge/pyton-3.6%20-brightgreen.svg)


# tcp_server.py
* 首先，创建一个基于IPv4和TCP协议的Socket：
```bash
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
* 然后，要绑定监听的地址和端口：
```bash
sock.bind(server_address)
```
* 其次，调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
```bash
print('starting listen on ip %s, port %s'%server_address)
sock.listen(1)
```
* 接下来，服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接:
```bash
  while True:
    print("waiting for connection")
    client,addr = sock.accept()
    print("having a connection")
    client.close()
```

# tcp_client.py
