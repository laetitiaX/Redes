import http.client

HOST = "localhost"
PORT = 8888
# criando um objeto do tipo HTTPConnection
conn = http.client.HTTPConnection(HOST, PORT)

# criando um pedido
conn.request("GET", "/Redes/index1.html")

r1 = conn.getresponse()

print(r1.status, r1.reason)