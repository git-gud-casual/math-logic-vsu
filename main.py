import matrix
import time


if __name__ == '__main__':
    a = []
    with open("13.txt") as f:
        for line in f.readlines():
            a.append(list(map(int, line.split())))

    start_time = time.time()
    result = matrix.determinant(a)
    final_time = time.time()

    print(result)
    print(f"Time: {final_time - start_time} seconds")


