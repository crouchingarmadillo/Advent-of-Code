from typing import Iterator, List

def get_lines(file_name: str) -> Iterator[str]:
    with open(file_name) as f:
        for line in f:
            yield line

def is_safe(report: List[int]) -> bool:
    is_increasing = True
    for i in range(len(report) - 1):
        dif = report[i+1] - report[i]
        if dif < 1 or dif > 3:
            is_increasing = False
            break

    is_decreasing = True
    for i in range(len(report) - 1):
        dif = report[i] - report[i+1]
        if dif < 1 or dif > 3:
            is_decreasing = False
            break

    return is_increasing or is_decreasing

def solution_a(file_name: str) -> int:
    result = 0
    for line in get_lines(file_name):
        report = list(map(int, line.split()))
        if is_safe(report):
            result += 1

    return result

def solution_b(file_name: str) -> int:
    result = 0
    for line in get_lines(file_name):
        report = list(map(int, line.split()))
        if is_safe(report):
            result += 1
        else:
            for i in range(len(report)):
                new_report = report[:i]
                new_report.extend(report[i+1:])
                if is_safe(new_report):
                    result += 1
                    break

    return result

def main():
    file_name = "../input/2"
    print(f"solution a: {solution_a(file_name)}")
    print(f"solution b: {solution_b(file_name)}")

if __name__ == "__main__":
    main()
