from typing import BinaryIO
from binary_difference.differentiators.basic import BasicDifferentiator


def calculate_difference(old_file: BinaryIO, new_file: BinaryIO, diff_file: BinaryIO):
    while old_file.readable() or new_file.readable():
        byte1 = old_file.read(1)
        byte2 = new_file.read(1)
        if byte1 == byte2:
            if byte1 == b'':
                break
            diff_file.write(b'\x00')
        else:
            diff_file.write(byte2)


def make_diff_file(old_name: str, new_name: str, path: str = ''):
    old_file = open(path + old_name, 'rb')
    new_file = open(path + new_name, 'rb')
    diff_file = open(path + '{}->{}.diff'.format(old_name, new_name), 'wb')
    calculate_difference(old_file, new_file, diff_file)
    old_file.close()
    new_file.close()
    diff_file.close()

