from .tools import *


def test_basics():
    for generator in Generators:
        generate_files(generator)

        direct_calc_diff(calculate_difference)

        direct_recover(recover)

        assert filecmp.cmp(PATH + FILE2, PATH + RECOVER_FILE)

        manual_cmp(PATH + FILE2, PATH + RECOVER_FILE)


def test_make_file_diff():
    for generator in Generators:
        generate_files(generator)
        make_diff_file(FILE1, FILE2, path=PATH)
        make_recovery(FILE1, make_diff_name(FILE1, FILE2), path=PATH)
        manual_cmp(PATH + FILE2, PATH + make_recovery_name(FILE2))
