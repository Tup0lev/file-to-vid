# coding:utf-8
from binascii import hexlify, unhexlify

__author__ = 'kang'

def bytes_from_file(filename, chunksize=8192):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break


# convert bytes to hex
data = ''
for b in bytes_from_file('file.name'):
    data += hexlify(b)

# Convert python string
# data = ['"' + data[i:i + 70] + '"' for i in range(0, len(data), 70)]
# print(" \\\n".join(data))

# hex to bytes
bytes_data = unhexlify(data)

# create file from hex
fp = open("new.file.name", "wb+")
fp.write(unhexlify(data))
fp.close()
