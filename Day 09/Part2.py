with open("./Day 09/input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


def sign(x: int) -> int:
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def move_tail(head: list[int], tail: list[int]) -> list[int]:
    if any(abs(head[i] - tail[i]) > 1 for i in range(2)):
        tail = [tail[i] - sign(tail[i] - head[i]) for i in range(2)]

    return tail


if __name__ == "__main__":

    head = [0, 0]
    tails = [[0, 0]] * 9
    seen = set()
    for line in lines:
        direction, num = line.split()
        for _ in range(int(num)):
            match direction:
                case "R":
                    head[0] += 1
                case "L":
                    head[0] -= 1
                case "U":
                    head[1] += 1
                case "D":
                    head[1] -= 1

            tails[0] = move_tail(head, tails[0])
            for i in range(len(tails) - 1):
                tails[i + 1] = move_tail(tails[i], tails[i + 1])
            seen.add(tuple(tails[len(tails) - 1]))

    print(len(seen))
