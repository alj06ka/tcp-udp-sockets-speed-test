import random


class PacketGenerator:
    def __init__(self, seed=None, is_different=True):
        self.is_different = is_different
        self.seed = seed
        self.random = random
        self.reset_seed()

    def generate_packet(self, packet_size):
        if not self.is_different:
            self.reset_seed()
        byte_sequence = bytearray(self.random.getrandbits(8) for _ in range(packet_size))
        return byte_sequence

    def reset_seed(self):
        self.random.seed(self.seed)

class PacketValidator(PacketGenerator):
    def validate_packet(self, packet, packet_size):
        if packet == self.generate_packet(packet_size):
            return True
        return False
