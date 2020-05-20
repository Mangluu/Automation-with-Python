import socket



hostName    = "example.org"



ipAddress   = socket.gethostbyname(hostName)

print(ipAddress)
print(type(ipAddress))
