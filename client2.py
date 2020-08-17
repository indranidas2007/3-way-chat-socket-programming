import socket
s=socket.socket()
host=socket.gethostname()
port=8000
s.connect((host,port))
print("Connected to the server")
message= s.recv(1024)
message=message.decode()
print("Server message:", message)
while 1:
		message= s.recv(1024)
		message=message.decode()
		print("server:", message)
		message= s.recv(1024)
		message=message.decode()
		print("server:", message)
		new_msg= input(str(">>>"))
		new_msg= new_msg.encode()
		s.send(new_msg)
		print("Message sent")
		