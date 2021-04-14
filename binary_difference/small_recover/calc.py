from typing import BinaryIO
from binary_difference.differentiators.basic import BasicDifferentiator


def small_calc(old_file: BinaryIO, new_file: BinaryIO, diff_file: BinaryIO, diffor=BasicDifferentiator):
    old = old_file.read()
    new = new_file.read()
    diff_file.write(diffor.get_diff(old, new))


def small_file_diff(old_name: str, new_name: str, path: str = ''):
    old_file = open(path + old_name, 'rb')
    new_file = open(path + new_name, 'rb')
    diff_file = open(path + '{}->{}.diff'.format(old_name, new_name), 'wb')
    small_calc(old_file, new_file, diff_file)
    old_file.close()
    new_file.close()
    diff_file.close()

