import matrix
import time

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')


def get_int_list2_from_file(filename: str) -> list[list[int]]:
    a = []
    with open(filename) as f:
        for line in f.readlines():
            a.append(list(map(int, line.split())))
    return a


if __name__ == '__main__':
    """
    5х5 - 704
    10х10 - 194851613
    13х13 - 72986555176
    """
    args = parser.parse_args()
    arr = get_int_list2_from_file(args.filename)

    start_time = time.time()
    result = matrix.determinant(arr)
    final_time = time.time()

    print(result)
    print(f'Time: {final_time - start_time} seconds')


