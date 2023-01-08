import http.client
import socket
import sys

HOST = "localhost"
PORT = 8888

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


mysocket.connect((HOST, PORT))

mysocket.send(b'GET /pages/index1.html HTTP/1.0\r\nHost: localhost\r\n\r\n')

while True:
    data = mysocket.recv(512)
    if (len(data) < 1):
        break
    print(data)