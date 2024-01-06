import os, binascii
import struct
import argparse

# 인자 파서를 생성
parser = argparse.ArgumentParser(description='Process a PNG file.')
parser.add_argument('filepath', type=str, help='The path to the PNG file to process.')
parser.add_argument('crc32', type=str, help='The CRC32 to match. Input as four byte hex string.')

# 인자를 파싱
args = parser.parse_args()

# CRC32 값을 바이트로 변환
crc32_target = int(args.crc32.replace(' ', ''), 16)

# 파일을 읽으세요
with open(args.filepath, "rb") as f:
    misc = f.read()

for i in range(2000):
    for j in range(2000):
        data = misc[12:16] + struct.pack('>i',i) + struct.pack('>i',j) + misc[24:29]
        crc32 = binascii.crc32(data) & 0xffffffff
        if crc32 == crc32_target:
            print("Width : {}, Height : {}".format(' '.join([f'{i:02X}' for i in struct.pack('>I', i)]), ' '.join([f'{j:02X}' for j in struct.pack('>I', j)])))
