with open("./Day 13/input.txt", "r") as f:
    lines = [eval(line.strip()) for line in f.readlines() if line.strip() != ""]


# 1 if ascending, -1 if descending, 0 if same
def check(a, b):
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


if __name__ == "__main__":
    line_pairs = [lines[i : i + 2] for i in range(0, len(lines), 2)]

    result = sum(i for i, pair in enumerate(line_pairs, start=1) if check(*pair) == 1)

    print(result)
