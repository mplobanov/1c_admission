from .list_logic import list_and


def make_diff_name(old: str, new: str) -> str:
    assert '>' not in old, 'filenames with > are not supperted yet'
    assert '>' not in new, 'filenames with > are not supperted yet'
    return "{}->{}.diff".format(old, new)


def check_diff_name(old: str, diff: str) -> bool:
    conditions = [
        diff.endswith('.diff'),
        diff.startswith("{}->".format(old)),
    ]
    return list_and(conditions)


def get_new_filename(old: str, diff: str) -> str:
    return diff[diff.rindex('>') + 1: diff.rindex('.diff')]


def make_recovery_name(new: str) -> str:
    return '{}.recovered'.format(new)
