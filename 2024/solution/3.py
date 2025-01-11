import re

# number = 0 | [1-9][0-9]*
mul = re.compile("mul\((0|([1-9][0-9]*)),(0|([1-9][0-9]*))\)")
dont_do_mul = re.compile("(do\(\))|(don't\(\))|(mul\((0|([1-9][0-9]*)),(0|([1-9][0-9]*))\))")

def part1(filename: str) -> int:
    result = 0
    with open(filename, "r") as f:
        for multiplication in mul.findall(f.read()):
            x = int(multiplication[1])
            y = int(multiplication[2])
            result += x * y
    return result

def part2(filename: str) -> int:
    result = 0
    do = True
    with open(filename, "r") as f:
        for match in dont_do_mul.finditer(f.read()):
            s = match.group(0)
            if s == "don't()":
                do = False
            elif s == "do()":
                do = True
            elif do:
                s0, s1 = list(s.split(','))
                x = int(s0[4:])
                y = int(s1[:len(s1)-1])
                result += x * y

    return result

def main():
    filename = "input/3"
    print(f"part1: {part1(filename)}")
    print(f"part2: {part2(filename)}")

if __name__ == "__main__":
    main()
