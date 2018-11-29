import socket
import sys
def start_tcp_client(ip, port):
  #server port and ip
  server_ip = ip
  servr_port = port
  tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    tcp_client.connect((server_ip, server_port))
  except:
    print("fail to setup socket connection")
  tcp_client.close()
  if __name__ == '__main__':
    start_tcp_clien('192.168.0.107', 12345)