import sys
import numpy as np


def main(filename):
    f = np.fromfile(open(filename), dtype=np.complex64)

    l = len(f)
    i = 0
    while i < l:
        first = f[i]
        second = f[i+1]
        print("{:f},{:f},{:f},{:f}".format(first.real, first.imag, second.real, second.imag))
        i = i + 2

if __name__ == '__main__':
    main(sys.argv[1])
