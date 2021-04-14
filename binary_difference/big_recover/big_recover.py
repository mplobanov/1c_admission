from typing import BinaryIO
from binary_difference.utils.filenames import *


def recover(old_file: BinaryIO, diff_file: BinaryIO, new_file: BinaryIO):
    old_byte = old_file.read(1)
    while old_byte != b'':
        diff_byte = diff_file.read(1)
        if diff_byte == b'\x00':
            new_file.write(old_byte)
        else:
            new_file.write(diff_byte)
        old_byte = old_file.read(1)


def make_recovery(old_name: str, diff_name: str, path: str = ''):
    # check for valid name
    assert check_diff_name(old_name, diff_name)

    old_file = open(path + old_name, 'rb')
    diff_file = open(path + diff_name, 'rb')
    recovery_file = open(path + make_recovery_name(get_new_filename(old_name, diff_name)), 'wb')

    recover(old_file, diff_file, recovery_file)

    old_file.close()
    diff_file.close()
    recovery_file.close()
