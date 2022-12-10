with open("./Day 5/input.txt", "r") as f:
    L = [
        ["D", "H", "R", "Z", "S", "P", "W", "Q"],
        ["F", "H", "Q", "W", "R", "B", "V"],
        ["H", "S", "V", "C"],
        ["G", "F", "H"],
        ["Z", "B", "J", "G", "P"],
        ["L", "F", "W", "H", "J", "T", "Q"],
        ["N", "J", "V", "L", "D", "W", "T", "Z"],
        ["F", "H", "G", "J", "C", "Z", "T", "D"],
        ["H", "B", "M", "V", "P", "W"],
    ]

    L = [list(reversed(L[i])) for i in range(len(L))]

    def move_one(start: int, end: int) -> None:
        L[end - 1].append(L[start - 1].pop())

    def move(n: int, start: int, end: int) -> None:
        [move_one(start, end) for _ in range(n)]

    [
        move(
            *(
                map(
                    int,
                    line.replace("move ", "")
                    .replace("from ", "")
                    .replace("to ", "")
                    .split(),
                )
            )
        )
        for line in f.readlines()[10:]
    ]

    [print(l[-1], end="") for l in L]
