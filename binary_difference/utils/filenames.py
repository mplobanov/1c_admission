from .list_logic import list_and


def make_diff_name(old: str, new: str) -> str:
    return "{}->{}.diff".format(old, new)


def check_diff_name(old: str, diff: str) -> bool:
    conditions = [
        diff.endswith('.diff'),
        diff.startswith("{}->".format(old)),
    ]
    return list_and(conditions)
