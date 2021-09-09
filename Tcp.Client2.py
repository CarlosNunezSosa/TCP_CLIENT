import socket

target = "localhost"
port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target, port))
inputUsername = input("Username: ")
inputPassword = input("Password: ")
infoToSend = inputUsername + ";"+inputPassword
client.send(infoToSend.encode("utf-8"))

response = client.recv(4096)

print(response.decode("utf-8"))