# import socket
# import time

# HOST = '127.0.0.1'
# PORT = 8080

# BUFSIZE = 1024
# ADDR = (HOST,PORT)


# #1 서버에 접속하기 위한 소켓을 생성한다.
# clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# #2. 서버에 접속을 시도한다.
# clientSocket.connect(ADDR)
# print('connect is success')


# import socket
# from select import select
# import time

# HOST = "127.0.0.1"
# #HOST = "localhost"
# PORT = 8080

# BUFSIZE = 1024
# ADDR = (HOST,PORT)

# srvSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# srvSock.bind(('', PORT))
# srvSock.listen()

# cltSocket, addr = srvSock.accept()

# while True:
#     response = cltSocket.recv(1024)
#     print ('client : ', response.decode('utf-8'))

#     message = input('server : ')
#     cltSocket.send(message.encode('utf-8'))

# cltSocket.close()









# import socket
# import sys

# import time

# HOST = '127.0.0.1'
# PORT = 8080

# BUFSIZE = 1024
# ADDR = (HOST,PORT)

# clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# clientSocket.connect(ADDR)

# while True:
#     message = input('client : ')
#     clientSocket.send(message.encode('utf-8'))
#     response = clientSocket.recv(1024)
#     print ('server : ', response.decode('utf-8'))

# clientSocket.close()

# import socket

# HOST = "127.0.0.1"
# PORT = 1234

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind((HOST, PORT))

# while True:
#     data, addr = sock.recvfrom(1024)
#     print("msg: ", data)

#     rsp = data.decode("utf-8").upper()
#     sock.sendto(rsp.encode("utf-8"), addr)

# sock.close()

# 속성 출력 
# class Person :
#     name  = "python"
#     age   = 23
#     number = "01012345678"
    
# p = Person()
# print(p.name)
# print(p.age)
# print(p.number)

# p1 = Person
# print(p1.name)
# print(p1.age)
# print(p1.number)

# class Person :
# 	name = "python"
# 	age = 23
# 	number = "01012345678"

# 	def getIntroduce(self):
# 		return f"My name is {self.name}"


# p = Person()
# print(p.name)
# print(p.age)
# print(p.number)
# print(p.getIntroduce)


#클래스 초기화
# class Person :
# 	def __init__(self, name, age, number):
# 		self.name = name
# 		self.age = age
# 		self.number = number
# p = Person("Hello", 24, "01033333333")
# p1 = Person("He", 21, "01033555555")
# p2 = Person("hee", 24, "01040173919")
# print(p.name)
# print(p1.name)
# print(p2.name)

# print(p.number)
# print(p1.number)
# print(p2.number)

# print(p.age)
# print(p1.age)
# print(p2.age)



class Person :
	count = 0
	
	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.number = number
		Person.count +=1

p = Person("Hello", 24, "01033333333")
p1 = Person("He", 21, "01033555555")
p2 = Person("hee", 24, "01040173919")



p = Person("Hello", 24, "01033333333")
print(p.name)
print(p.count)

p1 = Person("He", 21, "01033555555")
print(p1.name)
print(p1.count)

p2 = Person("hee", 24, "01040173919")
print(p2.name)
print(p2.count)







