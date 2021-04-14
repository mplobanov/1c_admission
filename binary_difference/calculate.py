from typing import BinaryIO


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