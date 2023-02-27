import socket

# Create a socket and listen for incoming connections
s = socket.socket()
receiver_address = ('', 12345)  # Use an empty string for the IP address to listen on all available interfaces
s.bind(receiver_address)
s.listen()

# Wait for a client to connect
print('Waiting for connection...')
client_socket, client_address = s.accept()
print(f'Connection from {client_address}')

# Receive the IP address from the client
data = client_socket.recv(1024)
ipv4_address = data.decode()
print(f'Received IP address: {ipv4_address}')

# Close the client socket and server socket
client_socket.close()
s.close()

