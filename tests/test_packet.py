import unittest
import struct
import ipaddress
from typing import List
from dhcppython import packet
from dhcppython import options


class PacketTestCases(unittest.TestCase):
    def test_parse_discover1(self):
        self.assertEqual(
            packet.DHCPPacket.from_bytes(discover_linux).asbytes,
            discover_linux
        )
    def test_parse_discover2(self):
        self.assertEqual(
            packet.DHCPPacket.Discover(
                "8c:45:00:1d:48:16",
                seconds=1,
                tx_id=0xeabec397,
                use_broadcast=False,
                option_list=[
                    options.options.short_value_to_object(61, {'hwtype': 1, 'hwaddr': '8C:45:00:1D:48:16'}),
                    options.options.short_value_to_object(57, 1500),
                    options.options.short_value_to_object(60, "android-dhcp-9"),
                    options.options.short_value_to_object(12, "Galaxy-S9"),
                    options.options.short_value_to_object(55, [1, 3, 6, 15, 26, 28, 51, 58, 59, 43])
                ]
            ).asbytes,
            discover_android
        )
    def test_parse_offer1(self):
        self.assertEqual(
            packet.DHCPPacket.from_bytes(offer_linux).asbytes,
            offer_linux
        )
    def test_parse_request1(self):
        self.assertEqual(
            packet.DHCPPacket.from_bytes(request_linux).asbytes,
            request_linux
        )
    def test_parse_request2(self):
        self.assertEqual(
            packet.DHCPPacket.from_bytes(request_android_bytes).asbytes,
            request_android_bytes
        )
    def test_parse_ack1(self):
        self.assertEqual(
            packet.DHCPPacket.from_bytes(ack_linux).asbytes,
            ack_linux
        )


request_android: List[int] = [
    0x01, 0x01, 0x06, 0x00, 0xea, 0xbe,
    0xc3, 0x97, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x8c, 0x45,
    0x00, 0x1d, 0x48, 0x16, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x63, 0x82, 0x53, 0x63, 0x35, 0x01, 0x03, 0x3d, 0x07, 0x01,
    0x8c, 0x45, 0x00, 0x1d, 0x48, 0x16, 0x32, 0x04, 0xc0, 0xa8, 0x01, 0xa6,
    0x36, 0x04, 0xc0, 0xa8, 0x01, 0xfe, 0x39, 0x02, 0x05, 0xdc, 0x3c, 0x0e,
    0x61, 0x6e, 0x64, 0x72, 0x6f, 0x69, 0x64, 0x2d, 0x64, 0x68, 0x63, 0x70,
    0x2d, 0x39, 0x0c, 0x09, 0x47, 0x61, 0x6c, 0x61, 0x78, 0x79, 0x2d, 0x53,
    0x39, 0x37, 0x0a, 0x01, 0x03, 0x06, 0x0f, 0x1a, 0x1c, 0x33, 0x3a, 0x3b,
    0x2b, 0xff
]
request_android_bytes: bytes = struct.pack(
    ">" + len(request_android) * "B", *request_android
)

discover_android = (
    b"\x01\x01\x06\x00\xea\xbe"
    b"\xc3\x97\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x8c\x45\x00\x1d\x48\x16\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x63\x82\x53\x63\x35\x01\x01\x3d\x07\x01"
    b"\x8c\x45\x00\x1d\x48\x16\x39\x02\x05\xdc\x3c\x0e\x61\x6e\x64\x72"
    b"\x6f\x69\x64\x2d\x64\x68\x63\x70\x2d\x39\x0c\x09\x47\x61\x6c\x61"
    b"\x78\x79\x2d\x53\x39\x37\x0a\x01\x03\x06\x0f\x1a\x1c\x33\x3a\x3b"
    b"\x2b\xff"

)

discover_linux = (
    b"\x01\x01\x06\x00\x2e\xf9"
    b"\x31\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x08\x00\x27\x92\x1f\xae\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x63\x82\x53\x63\x35\x01\x01\x32\x04\xc0"
    b"\xa8\x38\x03\x0c\x05\x6d\x61\x72\x69\x6f\x37\x0d\x01\x1c\x02\x03"
    b"\x0f\x06\x77\x0c\x2c\x2f\x1a\x79\x2a\xff\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00"
).strip(b"\x00")
offer_linux = (
    b"\x02\x01\x06\x00\x2e\xf9"
    b"\x31\x7f\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xa8\x38\x03\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x08\x00\x27\x92\x1f\xae\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x63\x82\x53\x63\x01\x04\xff\xff\xff\x00"
    b"\x03\x04\x0a\x97\x01\x01\x06\x04\x0a\x68\x01\x08\x0c\x09\x6d\x61"
    b"\x72\x69\x6f\x2e\x63\x6f\x6d\x0f\x0e\x73\x77\x65\x65\x74\x77\x61"
    b"\x74\x65\x72\x2e\x63\x6f\x6d\x33\x04\x00\x01\x51\x80\x35\x01\x02"
    b"\x36\x04\xc0\xa8\x38\x02\x3a\x04\x00\x00\x54\x60\x3b\x04\x00\x00"
    b"\xa8\xc0\xff"
).strip(b"\x00")
request_linux = (
    b"\x01\x01\x06\x00\x2e\xf9"
    b"\x31\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x08\x00\x27\x92\x1f\xae\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x63\x82\x53\x63\x35\x01\x03\x36\x04\xc0"
    b"\xa8\x38\x02\x32\x04\xc0\xa8\x38\x03\x0c\x05\x6d\x61\x72\x69\x6f"
    b"\x37\x0d\x01\x1c\x02\x03\x0f\x06\x77\x0c\x2c\x2f\x1a\x79\x2a\xff"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00"
).strip(b"\x00")
ack_linux = (
    b"\x02\x01\x06\x00\x2e\xf9"
    b"\x31\x7f\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xa8\x38\x03\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x08\x00\x27\x92\x1f\xae\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x63\x82\x53\x63\x01\x04\xff\xff\xff\x00"
    b"\x03\x04\x0a\x97\x01\x01\x06\x04\x0a\x68\x01\x08\x0c\x09\x6d\x61"
    b"\x72\x69\x6f\x2e\x63\x6f\x6d\x0f\x0e\x73\x77\x65\x65\x74\x77\x61"
    b"\x74\x65\x72\x2e\x63\x6f\x6d\x33\x04\x00\x01\x51\x80\x35\x01\x05"
    b"\x36\x04\xc0\xa8\x38\x02\x3a\x04\x00\x00\x54\x60\x3b\x04\x00\x00"
    b"\xa8\xc0\xff"
).strip(b"\x00")


if __name__ == "__main__":
    unittest.main()