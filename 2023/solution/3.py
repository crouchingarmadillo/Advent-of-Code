# Part One (Time: >24H) (Rank: 154716)
# Input: File of numbers and symbols, separated by '.'
# Output: Sum of the numbers adjacent to a symbol (this includes diagonal)

# Checks if a character is a symbol (well if python had characters)
def is_symbol(s: str) -> bool:
    return not(s.isdigit() or s=='.')

# Checks if in a given region on a line (start inclusive to end exclusive) there is a symbol adjacent to the region 
def has_symbol(line: str, start: int, end: int) -> bool:
    if start == 0 and end == len(line):
        return len([c for c in line if is_symbol(c)]) != 0
    elif start == 0:
        return len([c for c in line[:end+1] if is_symbol(c)]) != 0
    elif end == len(line):
        return len([c for c in line[start-1:] if is_symbol(c)]) != 0
    else:
        return len([c for c in line[start-1:end+1] if is_symbol(c)]) != 0
       

# Given a line, finds the regions specifying numbers
def dig_locs(line: str) -> list[tuple[int, int]]:
    result = []
    start = 0

    while start < len(line):
        if line[start].isdigit():
            for end in range(start+1, len(line)+1):
                if end == len(line) or (end!=len(line) and not line[end].isdigit()):
                    result.append((start, end))
                    start = end
                    break
        else:
            start += 1

    return result

def solution1(lines: list[str]) -> int:
    count = 0

    for i, line in enumerate(lines):
        dig_locations = dig_locs(line)

        if i == 0:
            for start, end in dig_locations:
                if has_symbol(lines[i + 1], start, end) or has_symbol(line, start, end):
                    count += int(line[start:end])

        elif i == len(lines) - 1:
            for start, end in dig_locations:
                if has_symbol(lines[i - 1], start, end) or has_symbol(line, start, end):
                    count += int(line[start:end])
        else:
            for start, end in dig_locations:
                if has_symbol(lines[i + 1], start, end) or has_symbol(lines[i - 1], start, end) or has_symbol(line, start, end):
                    count += int(line[start:end])

    return count

# Part Two (Time: >24H) (Rank: 133995)
# Input: Same as Part One but now declare '*' symbols to be "gears". 
# When exactly two numbers are adjacent to a gear, their product is called the "gear ratio".
# Output: Sum of the gear ratios

# Checks if the location of a gear is adjacent to the region of a number
def has_gear(start: int, end: int, loc: int) -> bool:
    at_beg = loc == start - 1
    at_end = loc == end
    at_mid = start <= loc and loc < end

    return at_beg or at_end or at_mid

# Given a location (loc) for a gear, returns the gear ratio if it exists and None otherwise.
def gear_ratio(line: str, line_top: str, line_bot: str, loc: int) -> int | None:
    gears = []
    locs0 = dig_locs(line)
    locs1 = dig_locs(line_top)
    locs2 = dig_locs(line_bot)

    for start, end in locs0:
        if has_gear(start, end, loc):
            gears.append(int(line[start:end]))

    for start, end in locs1:
        if has_gear(start, end, loc):
            gears.append(int(line_top[start:end]))

    for start, end in locs2:
        if has_gear(start, end, loc):
            gears.append(int(line_bot[start:end]))

    if len(gears) == 2:
        return gears[0] * gears[1]
    else:
        return None

# Modified gear_ratio function for the first and last lines
def gear_ratio1(line: str, line_adj: str, loc: int) -> int | None:
    gears = []
    locs0 = dig_locs(line)
    locs1 = dig_locs(line_adj)

    for start, end in locs0:
        if has_gear(start, end, loc):
            gears.append(int(line[start:end]))

    for start, end in locs1:
        if has_gear(start, end, loc):
            gears.append(int(line_adj[start:end]))

    if len(gears) == 2:
        return gears[0] * gears[1]
    else:
        return None

def solution2(lines: list[str]) -> int:
    count = 0

    for i, line in enumerate(lines):
        if i == 0:
            for loc, s in enumerate(line):
                if s == "*":
                    ratio = gear_ratio1(line, lines[i+1], loc)
                    if ratio != None:
                        count += int(ratio)
        elif i == len(lines) - 1:
            for loc, s in enumerate(line):
                if s == "*":
                    ratio = gear_ratio1(line, lines[i-1], loc)
                    if ratio != None:
                        count += int(ratio)
        else:
            for loc, s in enumerate(line):
                if s == "*":
                    ratio = gear_ratio(line, lines[i-1], lines[i+1], loc)
                    if ratio != None:
                        count += int(ratio)

    return count

def main():
    with open("input/3.txt") as f:
        inpt = f.read().splitlines()

    print("solution 1:", solution1(inpt))
    print("solution 2:", solution2(inpt))

if __name__ == "__main__" :
    main()
