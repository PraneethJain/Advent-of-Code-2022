with open("./Day 6/input.txt", "r") as f:
    packet = f.read()
    for i, letter in enumerate(packet[14:], start=14):
        if len(set(packet[i - 14 : i])) == 14:
            print(i)
            break
