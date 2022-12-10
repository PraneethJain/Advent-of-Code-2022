result = 0
mapping = {"X": 1, "Y": 2, "Z": 3}
with open("./Day 2/input.txt", "r") as f:
    for line in f.readlines():
        p1, p2 = line.split()
        result += mapping[p2]
        if (
            (p1 == "A" and p2 == "X")
            or (p1 == "B" and p2 == "Y")
            or (p1 == "C" and p2 == "Z")
        ):
            result += 3
        elif (
            (p1 == "A" and p2 == "Y")
            or (p1 == "B" and p2 == "Z")
            or (p1 == "C" and p2 == "X")
        ):
            result += 6
        else:
            result += 0

print(result)
