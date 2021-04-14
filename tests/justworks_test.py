from random import choice, randint
from binary_difference.calculate import calculate_difference
from binary_difference.recogit ver import recover
import os


FILE1 = 'examples/files/file1'
FILE2 = 'examples/files/file2'
DIFF_FILE = 'examples/files/file1_diff_file2'
RECOVER_FILE = 'examples/files/file2_recovered'

PATH = '/Users/mplobanov/PycharmProjects/binary_diff/'
# PATH = ''


def test_basics():
    print('HELL', os.getcwd())
    old_file = open(PATH + FILE1, 'w')
    new_file = open(PATH + FILE2, 'w')
    for i in range(10):
        x = randint(0, 9)
        old_file.write(str(x))
        if choice([1, 0]):
            new_file.write(str(x))
        else:
            new_file.write(str(randint(0, 9)))
    old_file.write('\n')
    new_file.write('\n')
    old_file.close()
    new_file.close()

    old_file = open(PATH + FILE1, 'rb')
    new_file = open(PATH + FILE2, 'rb')
    diff_file = open(PATH + DIFF_FILE, 'wb')
    calculate_difference(old_file, new_file, diff_file)
    old_file.close()
    new_file.close()
    diff_file.close()

    old_file = open(PATH + FILE1, 'rb')
    diff_file = open(PATH + DIFF_FILE, 'rb')
    recovered_file = open(PATH + RECOVER_FILE, 'wb')
    recover(old_file, diff_file, recovered_file)
    old_file.close()
    diff_file.close()
    recovered_file.close()

    recovered_file = open(PATH + RECOVER_FILE, 'rb')
    new_file = open(PATH + FILE2, 'rb')
    while True:
        b1 = recovered_file.read(1)
        b2 = new_file.read(1)
        assert b1 == b2
        if b1 == b'':
            break
