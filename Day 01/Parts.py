with open("./Day 01/input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

L = []
cur_sum = 0
for line in lines:
    if line == "":
        L.append(cur_sum)
        cur_sum = 0
    else:
        cur_sum += int(line)

L.sort(reverse=True)

print(f"Highest is {L[0]}")
print(f"Sum of 3 highest is {sum(L[:3])}")
