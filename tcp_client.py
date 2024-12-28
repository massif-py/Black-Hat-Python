import ssl
import socket

target_host = 'aulavirtual.utel.edu.mx'
target_port = 443

# Create a socket object.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Create an SSL context.
context = ssl.create_default_context()

# Connect to the HTTPS server and establish the secure connection.
client = context.wrap_socket(client, server_hostname=target_host)

# Connect the client.
client.connect((target_host, target_port))

# Send some data.
client.send(b'GET / HTTP/1.1\r\nHost: aulavirtual.utel.edu.mx\r\n\r\n')

# Receive some data.
response = client.recv(4096)
print(response.decode())

# Close the connection.
client.close()