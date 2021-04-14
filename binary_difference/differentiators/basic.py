from copy import copy


class BasicDifferentiator:
    def __init__(self):
        pass

    # makes part of diff file
    def get_diff(self, old: bytes, new: bytes) -> bytes:
        ans = copy(bytearray(new))
        for i in range(len(old)):
            if old[i] == ans[i]:
                ans[i] = 0
        return bytes(ans)

    def get_recovered(self, old: bytes, diff: bytes) -> bytes:
        ans = copy(bytearray(diff))
        for i in range(len(old)):
            if ans[i] == 0:
                ans[i] = old[i]
        return ans
