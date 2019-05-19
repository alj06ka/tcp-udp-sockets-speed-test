import socket

from packets import PacketGenerator

HOST = 'localhost'
PORT = 65433
PACKET_SIZE = 1024
DEFAULT_SEED = 10000
PACKET_COUNT = 10000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_listener:
    socket_listener.bind((HOST, PORT))
    backlog = 0
    socket_listener.listen(backlog)
    connection, address = socket_listener.accept()
    with connection:
        print(f'Connected by {address}')
        packet_generator = PacketGenerator(DEFAULT_SEED)
        for _ in range(PACKET_COUNT):
            packet = packet_generator.generate_packet(PACKET_SIZE)
            connection.sendall(packet)
        print('Packages sent successful')
