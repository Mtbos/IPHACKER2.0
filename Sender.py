import socket
import subprocess

# Retrieve the IP address
ip_process = subprocess.Popen(['ipconfig'], stdout=subprocess.PIPE)
output, error = ip_process.communicate()
ipv4_address = ''
for line in output.splitlines():
    line = line.strip().decode('utf-8')
    if line.startswith('IPv4 Address'):
        ipv4_address = line.split(': ')[1]

# Create a socket and connect to the receiver
s = socket.socket()
receiver_address = ('192.168.43.180', 12345)  # Replace with the IP address of the receiver and a desired port number
s.connect(receiver_address)

# Send the IP address to the receiver
s.send(ipv4_address.encode())

# Close the socket
s.close()

