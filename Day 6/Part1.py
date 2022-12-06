with open("input.txt", "r") as f:
    packet = f.read()
    for i, letter in enumerate(packet[4:], start=4):
        if len(set(packet[i - 4 : i])) == 4:
            print(i)
            break
