with open("inputs/03.in", "r") as file:
    data = file.read().splitlines()


def count_trees(trees, x_change, y_change):
    width = len(trees[0])
    treesFound = 0
    xpos = 0
    height = 0
    while height < len(trees):
        if trees[height][xpos % width] == "#":
            treesFound += 1
        xpos += x_change
        height += y_change
    return treesFound


print(count_trees(data, 3, 1))
print(count_trees(data, 1, 1)
      * count_trees(data, 3, 1)
      * count_trees(data, 5, 1)
      * count_trees(data, 7, 1)
      * count_trees(data, 1, 2))
