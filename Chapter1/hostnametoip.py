import socket
#defining values
target_host ="www.google.com"
target_port = 80

#getting ip address from hostname

r = socket.gethostbyname(target_host)
print(r)
