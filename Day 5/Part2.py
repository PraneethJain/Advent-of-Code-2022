with open("input.txt", "r") as f:
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

    def move(n: int, start: int, end: int) -> None:
        start_L = L[start - 1]
        end_L = L[end - 1]
        to_move_L = []
        [to_move_L.insert(0, start_L.pop()) for _ in range(n)]
        end_L.extend(to_move_L)

    [
        move(
            *map(
                int,
                line.replace("move ", "")
                .replace("from ", "")
                .replace("to ", "")
                .split(),
            )
        )
        for line in f.readlines()[10:]
    ]

    [print(l[-1], end="") for l in L]
