import socket
import threading

# Ip and Ports to connect to.
bind_ip = "0.0.0.0"
bind_port = 9999

# Server comes online and starts listening
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print("[*] Listening on %s:%d" % (bind_ip, bind_port))


# Opens the Data.txt file and returns all the content in it.
def readfile(filename):
    info = ""
    file = open(filename)
    for line in file:
        info = info + line
    return info


# Client/Server receives the information sent by the user then proceeds to save it in the existing file.
# Once finished it sends a message to the user letting them know that the data was received and saved.
def handler_client(client_socket):

    request = client_socket.recv(4096)
    text = readfile("Data")
    file = open("Data", "w")

    file.write(text + "\n" + request.decode("utf-8"))
    file.close()

    client_socket.send(b"Connection Successful and Username and Password Saved!")
    client_socket.close()


# This method enables the server program to not end, thus constantly listening and waiting for a client to connect.
# Once a client connects the program is enabled to finish once the user is finished with the connection.
def stand_by():
    while True:
        client, addr = server.accept()
        print("[*] Accepted connection from: %s %d" % (addr[0], addr[1]))
        client_handler = threading.Thread(target=handler_client, args=(client,))
        client_handler.start()


stand_by()
exit()