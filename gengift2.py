import struct
import sys

# We build the content of the file in a byte string first
# This lets us calculate the length for the header at the end
data = b''
data += b"A" * 32  # Merchant ID
data += b"B" * 32  # Customer ID
data += struct.pack("<I", 1)  # One record
# Record of type animation
data += struct.pack("<I", 8 + 32 + 256)  # Record size (4 bytes)
data += struct.pack("<I", 3)  # Record type (4 bytes)
data += b"A" * 31 + b'\x00'  # Note: 32 byte message

# hang: update pc by -3 for infinite loop
data += struct.pack("<B", 9)    # load into reg[arg1]
data += struct.pack("<b", -3)    # set arg1 to invalid number
data += struct.pack("<B", 1)    # set arg2 to valid number

# cov1: test nop
# data += b'\x00' * 3   # nop
# data += b'\x08' * 253  # Program made entirely of "end program" (256 bytes)

# cov2: test update mptr
# data += struct.pack("<B", 2)    # load into reg[arg1]
# data += struct.pack("<b", 1)    # set arg1 to invalid number
# data += struct.pack("<B", 0)    # set arg2 to valid number
# data += b'\x08' * 253  # Program made entirely of "end program" (256 bytes)

# crash
# data += b'\x00' * 256   # nop

f = open(sys.argv[1], 'wb')
datalen = len(data) + 4  # Plus 4 bytes for the length itself
f.write(struct.pack("<I", datalen))
f.write(data)
f.close()