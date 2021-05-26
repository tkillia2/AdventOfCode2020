"""
--- Day 3: Toboggan Trajectory ---
With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's
certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will
take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map 
(your puzzle input) of the open squares (.) and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome 
stability, the same pattern repeats to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your 
map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start 
by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position 
that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there 
was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you 
encounter?
"""
# open the file and store and then read it into lines
path = open("path.txt")
lines = path.readlines()
trees = []
# for loop trick to move right and down according to specified slope
# -- needed some help with this had not seen it before but pretty cool
for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    x = 0
    y = 0
    tree = 0
    while y <= len(lines) - 1: # each line ends in a new character 
        location = lines[y][x] # setting location to the 0,0 starting point
        if location == "#":    # adds one to the tree count
            tree += 1
        x += right # moving to the right the specified distance
        # making sure that we do not move to far and then resets it if so
        if x >= len(lines[0]) - 1:
            x = x - len(lines[0]) + 1
        # moved right and checked if out of bounds so no can go down in order
        # to check for another tree
        y += down
    # after going through all of the lines in the path.txt file which is 323
    # we append the total trees found
    trees.append(tree)
# Part 1 answer is the second number in this list -- corresponds with slopes
# from above
print(trees)
# Part 2 answer is taking the counts list and multiplying them all together
ans = 1 # this will store the product of all five tree counts
for tree in trees:
    ans *= tree
print(ans)
