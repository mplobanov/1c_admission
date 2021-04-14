from typing import BinaryIO


def recover(old_file: BinaryIO, diff_file: BinaryIO, new_file: BinaryIO):
    old_byte = old_file.read(1)
    while old_byte != b'':
        diff_byte = diff_file.read(1)
        if diff_byte == b'\x00':
            new_file.write(old_byte)
        else:
            new_file.write(diff_byte)
        old_byte = old_file.read(1)