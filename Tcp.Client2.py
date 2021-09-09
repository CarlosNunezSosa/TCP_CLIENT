import socket

# Where the client will connect
target = "localhost"
port = 9999


# Client being created
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Client connecting to the server
client.connect((target, port))

# Asking the user for a Username and Password
print(" -------------------------")
print("|  TCP CLIENT CONNECTION  |")
print(" -------------------------\n")
inputUsername = input("Username: ")
inputPassword = input("Password: ")

# Encodes the Data(Username and Password) to be sent to the Server
infoToSend = inputUsername + ";"+inputPassword
client.send(infoToSend.encode("utf-8"))

# Response that the Server sends back to the Client to prove the connection was successful
response = client.recv(4096)


# Prints the response received from the Server
print(response.decode("utf-8"))

exit()