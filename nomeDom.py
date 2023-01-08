import http.client
import socket
import sys

def HTTPclient(host,port):
    conn = http.client.HTTPConnection(host, port)
    L = int(input())
    for i in range(L):
        content = input()
        conn.request("GET", content)
        r1 = conn.getresponse()
        data1 = r1.read()
        print(data1.decode())