from socket import * 

server_address = ('localhost', 12000)
client_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input("Enter command (ADD:address,year or STOP): ")

    client_socket.sendto(message.encode('utf-8'), server_address)

    if message.upper() == "STOP":
        break

    response, server_address = client_socket.recvfrom(1024)
    print(f"Server response: {response.decode('utf-8')}")

client_socket.close()
