#For the purposes of breaking in or maintaining access to target machines, this module is all you really need.
import socket

print("lets try and build a TCP client")

target_host = "www.google.com"
target_port = 80

# creating socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client to srver
client.connect((target_host,target_port))

#send some data
request = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client.send(request.encode())

#recieve response
response = client.recv(4096)

print(response)