import struct

data = b"\x0F"

a = struct.unpack("b", data)

print(a)
