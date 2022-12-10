with open("./Day 10/input.txt", "r") as f:
    x = 1
    cycle = 1
    lines = [line.strip() for line in f.readlines()]
    result = 0

    def do_cycle(cycle: int, x: int):
        global result
        result += cycle * x if cycle % 40 == 20 else 0
        return cycle + 1

    for line in lines:
        cycle = do_cycle(cycle, x)
        if line != "noop":
            cycle = do_cycle(cycle, x)
            x += int(line.split()[-1])

    print(result)
