import socket
outside = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
inside = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
outside.bind(("0.0.0.0", 7890))
while True
    data, addr = outside.recvfrom(10000)
    print("data: {0}".format(data))
