from random import randint


def randbytes(n: int) -> bytes:
    ans = bytes(0)
    for i in range(n):
        ans += randint(0, 255).to_bytes(1, byteorder='big')
    return ans
