import socket
import time

from packets import PacketValidator

HOST = 'localhost'
PORT = 65433
PACKET_SIZE = 1024
DEFAULT_SEED = 10000
PACKET_COUNT = 10000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as connection:
    connection.sendto(b'1', (HOST, PORT))
    validator = PacketValidator(DEFAULT_SEED, is_different=True)
    received_packets = {
        'valid': 0,
        'invalid': 0
    }

    print('Testing download speed...')
    connection.sendto(b'0', (HOST, PORT))
    start_receive_time = time.time()
    for _ in range(PACKET_COUNT):
        connection.sendto(b'1', (HOST, PORT))
        packet, address = connection.recvfrom(PACKET_SIZE)
        if validator.validate_packet(packet, PACKET_SIZE):
            received_packets['valid'] += 1
        else:
            received_packets['invalid'] += 1

    connection.sendto(b'0', (HOST, PORT))
    end_receive_time = time.time()
    speed = (PACKET_SIZE * PACKET_COUNT) / (end_receive_time - start_receive_time)
    print("Download speed: %0.4f" % (speed / 1000), ' Kb/s')
    print('Valid / invalid packets: ', received_packets['valid'], '/', received_packets['invalid'])
