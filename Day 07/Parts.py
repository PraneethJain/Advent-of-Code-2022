root = {}
with open("./Day 07/input.txt", "r") as f:
    cur_dir = root
    lines = [line.strip() for line in f.readlines()[1:]]
    for line in lines:
        if line.startswith("$"):
            command = line.split()[1:]
            if command[0] == "cd":
                cur_dir = cur_dir[command[1]]
        else:
            thing, name = line.split()
            cur_dir[name] = {"..": cur_dir} if thing == "dir" else int(thing)


result = 0
L = []


def get_size(dir):
    global result
    l = 0
    for k, v in dir.items():
        if k != "..":
            if isinstance(v, int):
                l += v
            else:
                l += get_size(v)
    if l <= 100000:
        result += l
    L.append(l)
    return l


total = get_size(root)
L.sort()

print(result)

for l in L:
    if l >= total - 40000000:
        print(l)
        break
