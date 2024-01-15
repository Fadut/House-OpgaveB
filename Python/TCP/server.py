from socket import *
import threading

# To use, start server and then client.
# Then type in the client.

def handle_client(connectionSocket, address):
    print (f"Connected from IP: {address[0]}")
    keep_communicating = True

    while keep_communicating:
        sentence = connectionSocket.recv(1024).decode()
        print(f"Received: {sentence}")

        # Split sentence into words
        words = sentence.split()

        if not words:
            break

        command = words[0].upper()

        if command == "ADD" and len(words) == 3:
            address_info = f"Address: {words[1]}, Year: {words[2]}"
            response = f"OK - {address_info}"
        elif command == "STOP":
            response = "STOPPING"
            break
        else:
            response = "Invalid request"

        connectionSocket.sendall(response.encode('utf-8')) 
    
    connectionSocket.close()
    print(f"Connection from {address} closed")

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(5)
print ("Server is ready to listen")

while True:
    connectionSocket, address = serverSocket.accept()
    threading.Thread(target = handle_client, args = (connectionSocket, address)).start()