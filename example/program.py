import time
from typing import Tuple


def fb(x: int, y: int) -> Tuple[int, int]:
    return y, x + y


def test() -> float:
    x: int = 0
    y: int = 1
    t: float = time.time()
    for i in range(1000000):
        x = 0
        y = 1
        for j in range(100):
            x, y = fb(x, y)
    return time.time() - t


print(test())
