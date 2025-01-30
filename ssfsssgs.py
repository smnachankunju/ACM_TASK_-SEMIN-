import base64
from itertools import cycle

c1_hex = "0e0a193c0802117f0007452b0300591a0714330b0a1a38111b"
c2_hex = "382c3824050e076e375d3a6f2d3a21491d2a6e2930372d2d38526f16"


c1_bytes = bytes.fromhex(c1_hex)
c2_bytes = bytes.fromhex(c2_hex)
print(c1_bytes)
print(c2_bytes)

test_plaintext = "Welcome to the CTF".encode()
print(test_plaintext)
key = bytes(a ^ b for a, b in zip(c1_bytes, test_plaintext))
flag_bytes = bytes(a ^ b for a, b in zip(c2_bytes, cycle(key)))
flag = flag_bytes.decode()

print("Recovered Flag:", flag)
