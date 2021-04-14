from copy import copy
import pickle


class DictDifferentiator:
    def __init__(self):
        pass

    # makes part of diff file
    def get_diff(self, old: bytes, new: bytes) -> bytes:
        dfs = dict()
        for i in range(len(new)):
            if i >= len(old):
                dfs[i] = new[i]
            else:
                if old[i] != new[i]:
                    dfs[i] = new[i]
        return pickle.dumps(dfs)

    def get_recovered(self, old: bytes, diff: bytes) -> bytes:
        dfs = pickle.loads(diff)
        ans = copy(bytearray(old))
        for key, value in dfs.items():
            while len(ans) >= key:
                ans.append(0)
            ans[key] = value
        return bytes(ans)
