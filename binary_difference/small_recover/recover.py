from typing import BinaryIO
from binary_difference.differentiators.basic import BasicDifferentiator


def small_calc_recover(old_file: BinaryIO, diff_file: BinaryIO, new_file: BinaryIO, diffor=BasicDifferentiator):
    old = old_file.read()
    diff = diff_file.read()
    new_file.write(diffor().get_recovered(old, diff))
