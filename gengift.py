# import struct
# import sys

# # We build the content of the file in a byte string first
# # This lets us calculate the length for the header at the end
# data = b''
# data += b"GiftCardz.com".ljust(32, b' ')  # Merchant ID
# data += b"B" * 32  # Customer ID
# data += struct.pack("<I", 1)  # One record
# # Record of a type message
# data += struct.pack("<I", 8 + 32)  # Record size: 4 bytes size, 4 bytes type, 32 bytes message
# data += struct.pack("<I", 2)  # Record type
# data += b"x" * 31 + b'\0'   

# f = open(sys.argv[1], 'wb')
# datalen = len(data) + 4  # Plus 4 bytes for the length itself
# f.write(struct.pack("<I", datalen))
# f.write(data)
# f.close()


# CRash 1
# import struct
# import sys

# # We build the content of the file in a byte string first
# # This lets us calculate the length for the header at the end
# data = b''
# data += b"GiftCardz.com".ljust(32, b' ') # Merchant ID
# data += b"B"*32 # Customer ID
# data += struct.pack("<I", 1) # One record
# # Record of type message
# data += struct.pack("<I", 8 + 32)       # Record size: 4 bytes size, 4 bytes type, 32 bytes message
# data += struct.pack("<I", 2)            # Record type
# data += b"x"*31 + b'\0'                 # Note: 32 byte message

# f = open(sys.argv[1], 'wb')
# # dl = len(data) + 4  
# dl = 0xFFFFFFFF
# f.write(struct.pack("<I", dl))
# f.write(data)
# f.close()

# Crash 2  
# import struct
# import sys

# # We build the content of the file in a byte string first
# data = b''
# data += b"GiftCardz.com".ljust(32, b' ')  # Merchant ID
# data += b"B" * 32  # Customer ID
# data += struct.pack("<I", 1)  # One record

# # Record of type message with an incorrect program causing out-of-bounds access
# data += struct.pack("<I", 8 + 32)  # Record size: 4 bytes size, 4 bytes type, 32 bytes message
# data += struct.pack("<I", 3)   
 
# program = b"\x01\x2f" 
# data += b"S" * 31 + b'\0'  # 32 byte message
# data += program  # Append the program

# with open(sys.argv[1], 'wb') as f:
#     datalen = len(data) + 4  # Plus 4 bytes for the length itself
#     f.write(struct.pack("<I", datalen))
#     f.write(data)

  
# hang 1
# import struct
# import sys

# # Basic setup for the gift card data
# data = b''
# data += b"ExploitCorp".ljust(32, b' ')  # Merchant ID, padded to 32 bytes
# data += b"C" * 32  # Customer ID, also 32 bytes
# data += struct.pack("<I", 1)  # Number of records: just one

# # Setup for the animated message record 
# record_size = 4 + 4 + 32 + 256
# data += struct.pack("<I", record_size)  # Record size
# data += struct.pack("<I", 3)  
# message = b"_-_." + b'\0' * (32 - len("_-_."))
# data += message
 
# p = b'\x09\xfd' + b'\x00' * (256 - 2)  # 
 
# data += p

# f = open(sys.argv[1], 'wb')
# datalen = len(data) + 4 
# f.write(struct.pack("<I", datalen))
# f.write(data)
# f.close()


# cov1.gft coerage increade to 31.5%
# import struct
# import sys 
# data = b"GiftCardz.com".ljust(32, b' ')
# data += b"B" * 32
# data += struct.pack("<I", 1)  # One record
# data += struct.pack("<I", 8 + 32)  # Record size
# data += struct.pack("<I", 0xFF)  # Record type
# data += b"x" * 31 + b'\0'

# f = open(sys.argv[1], 'wb')
# datalen = len(data) + 4
# f.write(struct.pack("<I", datalen))
# f.write(data)
# f.close()

# cov2.gft  
# from cov2.gft  increase coverage to 34.21 %
# import struct
# import sys

# data = b"GiftCardz.com".ljust(32, b' ')
# data += b"B" * 32
# data += struct.pack("<I", 1)  # One record
# data += struct.pack("<I", 12)   
# data += struct.pack("<I", 3)  # Record type
# data += b"x" * 31  

# f = open(sys.argv[1], 'wb')
# datalen = len(data) + 4
# f.write(struct.pack("<I", datalen))
# f.write(data)
# f.close()