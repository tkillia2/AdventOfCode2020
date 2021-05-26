path = open("path.txt")
lines = path.readlines()

for right, down in [(3,1)]:
    x_spot = 0
    y_spot = 0
    tree = 0
    while y_spot <= len(lines) - 1:
        spot = lines[y_spot][x_spot]
        if( spot == "#"):
            tree += 1
        x_spot += right #adds three
        # check if out of bounds
        if x_spot >= len(lines[0]) -1:
            x_spot = x_spot - len(lines[0]) + 1
        y_spot += down # move down a row
    print(tree)

