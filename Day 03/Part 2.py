mapping = {chr(i + 96): i for i in range(1, 27)} | {
    chr(i + 64): i + 26 for i in range(1, 27)
}

with open("./Day 03/input.txt", "r") as f:
    result = 0
    lines = f.readlines()
    length = len(lines)
    for i in range(0, length, 3):
        a = (
            set(lines[i])
            .intersection(set(lines[i + 1]))
            .intersection(set(lines[i + 2]))
        )
        a.remove("\n")
        result += mapping[next(iter(a))]

    print(result)
