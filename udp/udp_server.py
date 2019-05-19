import socket

from packets import PacketGenerator

HOST = 'localhost'
PORT = 65433
PACKET_SIZE = 1024
DEFAULT_SEED = 10000
PACKET_COUNT = 10000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as socket_listener:
    socket_listener.bind((HOST, PORT))
    backlog = 0
    print('Server started')
    while True:
        request = socket_listener.recvfrom(1024)
        if request[0] == b'0':
            print('Starting speed test...')
            packet_generator = PacketGenerator(DEFAULT_SEED, is_different=True)
            address = request[1]
            packets_sent = 0
            print('Start sending packets to ', address)
            while socket_listener.recvfrom(1024)[0] != b'0':
                packet = packet_generator.generate_packet(PACKET_SIZE)
                socket_listener.sendto(packet, address)
                packets_sent += 1
            print('Packets sent: ', packets_sent)
            print('Packages sent successful')
