from random import choice, randint
from typing import TextIO, Callable, NoReturn

FILE1 = 'file1'
FILE2 = 'file2'
DIFF_FILE = 'file1_diff_file2'
RECOVER_FILE = 'file2_recovered'

PATH = '/Users/mplobanov/PycharmProjects/binary_diff/tests/files/'


def number_generator(old_file: TextIO, new_file: TextIO) -> NoReturn:
    for i in range(10):
        x = randint(0, 9)
        old_file.write(str(x))
        if choice([1, 0]):
            new_file.write(str(x))
        else:
            new_file.write(str(randint(0, 9)))


def diff_len_generator(old_file: TextIO, new_file: TextIO) -> NoReturn:
    for i in range(10):
        x = randint(0, 9)
        old_file.write(str(x))
        if choice([1, 0]):
            new_file.write(str(x))
        else:
            pass


Generators = [number_generator, diff_len_generator]


def generate_files(generator: Callable[[TextIO, TextIO], NoReturn] = number_generator):
    old_file = open(PATH + FILE1, 'w')
    new_file = open(PATH + FILE2, 'w')

    generator(old_file, new_file)

    old_file.write('\n')
    new_file.write('\n')
    old_file.close()
    new_file.close()


def direct_calc_diff(calc_func):
    old_file = open(PATH + FILE1, 'rb')
    new_file = open(PATH + FILE2, 'rb')
    diff_file = open(PATH + DIFF_FILE, 'wb')
    calc_func(old_file, new_file, diff_file)
    old_file.close()
    new_file.close()
    diff_file.close()


def direct_recover(recover_func):
    old_file = open(PATH + FILE1, 'rb')
    diff_file = open(PATH + DIFF_FILE, 'rb')
    recovered_file = open(PATH + RECOVER_FILE, 'wb')
    recover_func(old_file, diff_file, recovered_file)
    old_file.close()
    diff_file.close()
    recovered_file.close()


def manual_cmp(f1, f2):
    recovered_file = open(f1, 'rb')
    new_file = open(f2, 'rb')
    while True:
        b1 = recovered_file.read(1)
        b2 = new_file.read(1)
        assert b1 == b2
        if b1 == b'':
            break
    recovered_file.close()
    new_file.close()
