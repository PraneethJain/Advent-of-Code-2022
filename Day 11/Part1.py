monkeys = [
    {
        "items": [97, 81, 57, 57, 91, 61],
        "operation": lambda x: x * 7,
        "test": lambda x: (x % 11 == 0),
        "true": 5,
        "false": 6,
        "count": 0,
    },
    {
        "items": [88, 62, 68, 90],
        "operation": lambda x: x * 17,
        "test": lambda x: (x % 19 == 0),
        "true": 4,
        "false": 2,
        "count": 0,
    },
    {
        "items": [74, 87],
        "operation": lambda x: x + 2,
        "test": lambda x: (x % 5 == 0),
        "true": 7,
        "false": 4,
        "count": 0,
    },
    {
        "items": [53, 81, 60, 87, 90, 99, 75],
        "operation": lambda x: x + 1,
        "test": lambda x: (x % 2 == 0),
        "true": 2,
        "false": 1,
        "count": 0,
    },
    {
        "items": [57],
        "operation": lambda x: x + 6,
        "test": lambda x: (x % 13 == 0),
        "true": 7,
        "false": 0,
        "count": 0,
    },
    {
        "items": [54, 84, 91, 55, 59, 72, 75, 70],
        "operation": lambda x: x * x,
        "test": lambda x: (x % 7 == 0),
        "true": 6,
        "false": 3,
        "count": 0,
    },
    {
        "items": [95, 79, 79, 68, 78],
        "operation": lambda x: x + 3,
        "test": lambda x: (x % 3 == 0),
        "true": 1,
        "false": 3,
        "count": 0,
    },
    {
        "items": [61, 97, 67],
        "operation": lambda x: x + 4,
        "test": lambda x: (x % 17 == 0),
        "true": 0,
        "false": 5,
        "count": 0,
    },
]

for _ in range(20):
    for monkey in monkeys:
        for i, item in enumerate(monkey["items"]):
            result = monkey["operation"](item) // 3
            if monkey["test"](result):
                monkeys[monkey["true"]]["items"].append(result)
            else:
                monkeys[monkey["false"]]["items"].append(result)
        monkey["count"] += len(monkey["items"])
        monkey["items"].clear()


A = sorted([monkey["count"] for monkey in monkeys], reverse=True)

print(A[0] * A[1])
