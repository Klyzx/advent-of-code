with open("inputs/03.in", "r") as file:
    data = file.read().splitlines()


def countTrees(trees, xChange, yChange):
    width = len(trees[0])
    treesFound = 0
    xpos = 0
    height = 0
    while height < len(trees):
        if trees[height][xpos % width] == "#":
            treesFound += 1
        xpos += xChange
        height += yChange
    return treesFound


print(countTrees(data, 3, 1))
print(countTrees(data, 1, 1)
      * countTrees(data, 3, 1)
      * countTrees(data, 5, 1)
      * countTrees(data, 7, 1)
      * countTrees(data, 1, 2))
