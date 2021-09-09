# TCP_CLIENT & TCP_SERVER

A TCP Server that constantly listens for a TCP Client to connect. Once the client connects to the server, the server asks for a Username and Password.
Once the Username and Password are entered, the Data(Username and Password) gets encrypted and sent to the server. Once it reaches the server, the server decrypts the Data and stores it in a Data.txt file.
Once the Data is stored in the .txt file the server sends the client a confirmation that the connection was succesful and the Data has been saved and updated.

Future Plans invlove the server being able to accept connections from multiple clients, then the server will act as a browser once you have logged in with the correct credentials.
