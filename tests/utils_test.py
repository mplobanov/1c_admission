from binary_difference.utils.filenames import *
from binary_difference.utils.list_logic import *


def test_make_filename():
    old = 'a.txt'
    new = 'b.txt'
    assert make_diff_name(old, new) == 'a.txt->b.txt.diff'


def test_check_filename():
    assert check_diff_name('a.txt', 'a.txt->b.txt.diff')
    assert not check_diff_name('a.txt', 'a.txt->b.txt.doff')
    assert not check_diff_name('a.txt', 'b.txt->a.txt.diff')


def test_list_and():
    assert list_and([True, True, True])
    assert not list_and([True, False])
    assert not list_and([False, False])
