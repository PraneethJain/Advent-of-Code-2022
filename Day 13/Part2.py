with open("./Day 13/input.txt", "r") as f:
    lines = [eval(line.strip()) for line in f.readlines() if line.strip() != ""]


def check(a: list[int] | int, b: list[int] | int) -> int:
    """
    Returns:
    - 1 if a and b are in ascending order
    - -1 if a and b in descending order
    - 0 if they are same
    - -2 if input is invalid
    """
    if type(a) == int and type(b) == int:
        if a == b:
            return 0
        elif a < b:
            return 1
        else:
            return -1
    elif type(a) == list and type(b) == list:
        for i, j in zip(a, b):
            res = check(i, j)
            if res == 0:
                continue
            elif res == 1:
                return 1
            else:
                return -1
        else:
            if len(a) < len(b):
                return 1
            elif len(a) > len(b):
                return -1
            else:
                return 0
    elif type(a) == list and type(b) == int:
        return check(a, [b])
    elif type(a) == int and type(b) == list:
        return check([a], b)
    else:
        return -2


if __name__ == "__main__":

    lines.extend([[[2]], [[6]]])

    # Bubble sort using check
    for _ in range(len(lines)):
        for i in range(len(lines) - 1):
            if check(lines[i], lines[i + 1]) == -1:
                lines[i + 1], lines[i] = lines[i], lines[i + 1]

    print((lines.index([[2]]) + 1) * (lines.index([[6]]) + 1))
