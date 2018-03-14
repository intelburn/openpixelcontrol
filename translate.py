import socket
outside = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
inside = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
outside.bind(("0.0.0.0", 7890))
inside.connect(("127.0.0.1",7890))
while True:
    data, addr = outside.recvfrom(10000)
    print("data received from {0}".format(addr))
    inside.send(data)
