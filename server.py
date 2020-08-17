import socket
s=socket.socket()
host=socket.gethostname()
port=8000
s.bind((host,port))
s.listen(1)
print("Waiting for two connections, client1 and client2...")
conn, addr= s.accept()
print("Connected to client1!")
conn.send("Welcome to the server".encode())
print("Waiting for 2nd connection...")
conn1, addr= s.accept()
print("Connected to client2!")
conn1.send("Welcome to the server".encode())
while 1:
		message=input(str(">>>"))
		message=message.encode()
		conn.send(message)
		conn1.send(message)
		print("Message Sent...")
		recv_message=conn.recv(1024)
		print("client1:", recv_message.decode())
		conn1.send(recv_message)
		recv_message=conn1.recv(1024)
		print("client2:", recv_message.decode())
		conn.send(recv_message)