import numpy as np
from scipy.signal import convolve2d

def get_accessible(A: np.typing.NDArray) -> np.typing.NDArray:
    # Calculate number of neighbours with convolution
    kernel = np.array([[1,1,1],
                       [1,0,1],
                       [1,1,1]])
    neigh = convolve2d(A, kernel, mode='same', boundary='fill', fillvalue=0)

    accessible = A * (neigh < 4).astype(int)
    return accessible

def part1(ll: list[str]) -> str:
    A = np.array([[1 if c == '@' else 0 for c in line] for line in ll])

    accessible = get_accessible(A)
    return str(accessible.sum())

def part2(ll: list[str]) -> str:
    A = np.array([[1 if c == '@' else 0 for c in line] for line in ll])
    ret: int = 0
    accessible = np.zeros_like(A)

    while True:
        accessible = get_accessible(A)
        if accessible.sum() == 0:
            break
        ret += accessible.sum()
        A -= accessible
    return str(ret)
