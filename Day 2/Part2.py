result = 0
mapping = {"A": 1, "B": 2, "C": 3}

with open("./Day 2/input.txt", "r") as f:
    for line in f.readlines():
        p1, p2 = line.split()
        if p2 == "Z":
            result += 6
            if p1 == "A":
                result += 2
            elif p1 == "B":
                result += 3
            elif p1 == "C":
                result += 1
        elif p2 == "Y":
            result += 3
            result += mapping[p1]
        else:
            if p1 == "A":
                result += 3
            elif p1 == "B":
                result += 1
            else:
                result += 2


print(result)
