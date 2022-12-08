with open("./Day 8/input.txt", "r") as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]
    length = len(grid)

if __name__ == "__main__":
    A = set()
    for i in range(length):
        for j in range(length):
            if all(grid[i][j] > grid[k][j] for k in range(i + 1, length)):
                A.add((i, j))
            if all(grid[i][j] > grid[k][j] for k in range(i)):
                A.add((i, j))
            if all(grid[i][j] > grid[i][k] for k in range(j + 1, length)):
                A.add((i, j))
            if all(grid[i][j] > grid[i][k] for k in range(j)):
                A.add((i, j))
    print(len(A))
