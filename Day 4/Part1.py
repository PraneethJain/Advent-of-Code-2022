with open("./Day 4/input.txt") as f:
    result = 0
    for line in f.readlines():
        L1, L2 = [list(map(int, a.split("-"))) for a in line.split(",")]
        A1 = {i for i in range(L1[0], L1[1] + 1)}
        A2 = {i for i in range(L2[0], L2[1] + 1)}
        inter = A1.intersection(A2)
        if inter == set(A1) or inter == set(A2):
            result += 1

    print(result)
