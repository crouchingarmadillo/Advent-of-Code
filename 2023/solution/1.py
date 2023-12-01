# Part One (Time: 00:06:23) (Rank: 3011)
# Input: File of words separated by '\n'
# Words have an associated calibration value obtained by concactenating the 
# first and last digits.

# Output: Compute the sum of the calibration values.

# Grab the first digit in a line
def first_dig(s: str) -> int:
    for i in range(len(s)):
        if s[i].isdigit():
            return int(s[i])
        else:
            continue
    return -1

# Grab the last digit in a line
def last_dig(s: str) -> int:
    n = len(s)
    for i in range(n-1, -1, -1):
        if s[i].isdigit():
            return int(s[i])
        else:
            continue
    return -1

def solution_one(file_name: str) -> str:
    result = 0
    with open(file_name, encoding="utf-8") as f:
        for line in f:
            result += 10*first_dig(line) + last_dig(line)
    return result

# Part Two (Time: 01:10:16) (Rank: 7744)
# Input: File of words separated by '\n'
# Words have an associated calibration value as in Part One, 
# but now "one", "two", ..., "nine" count as digits as well.

# Output: Compute the sum of the calibration values.

# Grab the first digit (including the "one", "two", ..., "nine")
def fst_dig(s: str) -> int:
    n = len(s)
    for i in range(n):
        if s[i].isdigit():
            return int(s[i])
        elif i<n-3 and s[i:i+4] == "nine":
            return 9
        elif i<n-4 and s[i:i+5] == "eight":
            return 8
        elif i<n-4 and s[i:i+5] == "seven":
            return 7
        elif i<n-2 and s[i:i+3] == "six":
            return 6
        elif i<n-3 and s[i:i+4] == "five":
            return 5
        elif i<n-3 and s[i:i+4] == "four":
            return 4
        elif i<n-4 and s[i:i+5] == "three":
            return 3
        elif i<n-2 and s[i:i+3] == "two":
            return 2
        elif i<n-2 and s[i:i+3] == "one":
            return 1
        else:
            continue
    return -1
    
# Grab the second digit (including the "one", "two", ..., "nine")
def lst_dig(s: str) -> int:
    n = len(s)
    for i in range(n, 0, -1):
        if s[i-1].isdigit():
            return int(s[i-1])
        elif i>3 and s[i-4:i] == "nine":
            return 9
        elif i>4 and s[i-5:i] == "eight":
            return 8
        elif i>4 and s[i-5:i] == "seven":
            return 7
        elif i>2 and s[i-3:i] == "six":
            return 6
        elif i>3 and s[i-4:i] == "five":
            return 5
        elif i>3 and s[i-4:i] == "four":
            return 4
        elif i>4 and s[i-5:i] == "three":
            return 3
        elif i>2 and s[i-3:i] == "two":
            return 2
        elif i>0 and s[i-3:i] == "one":
            return 1
        else:
            continue
    return -1


def solution_two(file_name: str) -> str:
    result = 0
    with open(file_name, encoding="utf-8") as f:
        for line in f:
            result += 10*fst_dig(line) + lst_dig(line)

    return result

# Print the answers
if __name__ == "__main__":
    file_name = "../input/1.txt"
    print("solution one: ", solution_one(file_name))
    print("solution two: ", solution_two(file_name))