from unittest import TestCase

from clashroyalebuildabot.emulator.emulator import Emulator


class FakeCodec:
    def __init__(self):
        self.decoded_packets = []

    def parse(self, line):
        return [b"packet-1", b"packet-2"]

    def decode(self, packet):
        self.decoded_packets.append(packet)
        return [f"frame-{packet.decode()}"]


class EmulatorParserTests(TestCase):
    def test_decodes_every_packet_returned_by_parser(self):
        emulator = Emulator.__new__(Emulator)
        emulator.os_name = "windows"
        emulator.codec = FakeCodec()

        frame = emulator._get_last_frame(b"encoded-h264")

        self.assertEqual(frame, "frame-packet-2")
        self.assertEqual(
            emulator.codec.decoded_packets,
            [b"packet-1", b"packet-2"],
        )
