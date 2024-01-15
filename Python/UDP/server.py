from socket import *

server_address = ('localhost', 12000)
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(server_address)

print(f"UDP Server is ready to receive on {server_address}")

while True:
    data, client_address = server_socket.recvfrom(1024)

    request = data.decode('utf-8').upper()

    if request.startswith("ADD"):
        params = request.split(":")[1].split(",")
        if len(params) == 2:
            response = f"OK - Address: {params[0]}, Year: {params[1]}"
        else:
            response = "Invalid ADD request"
    elif request == "STOP":
        response = "STOPPING"
        break
    else:
        response = "Invalid request"

    server_socket.sendto(response.encode('utf-8'), client_address)

server_socket.close()
print("UDP Server is stopping")