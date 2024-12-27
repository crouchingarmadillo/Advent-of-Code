import sys
from collections import Counter

def solution_a(file_name: str):
    left_list = []
    right_list = []
    with open(file_name) as f:
        for line in f:
            l, r = list(map(int, line.split()))
            left_list.append(l)
            right_list.append(r)

    left_list.sort()
    right_list.sort()

    distances = map(lambda x: abs(x[0] - x[1]), zip(left_list, right_list))
    return sum(distances)

def solution_b(file_name: str):
    left_list = []
    right_list = []

    with open(file_name) as f:
        for line in f:
            l, r = list(map(int, line.split()))
            left_list.append(l)
            right_list.append(r)

    right_counter = Counter(right_list)

    total = 0
    for x in left_list:
        total += x * right_counter[x]

    return total


def main():
    file_name = "../input/1"
    print(f"solution a: {solution_a(file_name)}")
    print(f"solution b: {solution_b(file_name)}")

if __name__ == "__main__":
    main()
