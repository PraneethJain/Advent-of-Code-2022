mapping = {chr(i + 96): i for i in range(1, 27)} | {
    chr(i + 64): i + 26 for i in range(1, 27)
}

with open("./Day 03/input.txt", "r") as f:
    result = 0
    for line in f.readlines():
        mid = len(line) // 2
        left, right = set(line[:mid]), set(line[mid:])
        result += mapping[next(iter(left.intersection(right)))]

    print(result)
