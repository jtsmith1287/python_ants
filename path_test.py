
import pathfinder
from collections import namedtuple
import random
import time


map = []
for row in xrange(20):
    row = []
    for column in xrange(20):
        row.append("[%s]" % random.choice([" ", " ", " ", "W"]))
    map.append(row)


def distance(loc1, loc2):
    row1, col1 = loc1
    row2, col2 = loc2
    d_col = min(abs(col1 - col2), len(map[0]) - abs(col1 - col2))
    d_row = min(abs(row1 - row2), len(map) - abs(row1 - row2))
    return d_row + d_col

def passable(loc):
    row, col = loc
    if (row < 0) or (row > 19) or (col < 0) or (col > 19):
        return False
    if map[row][col] != "[W]":
        return True
    else:
        return False

def run():
    Game = namedtuple("Game", ["distance", "passable"])
    Ant = namedtuple("Ant", ["loc", "target"])
    game = Game(distance, passable)
    ant = Ant((0, 0), (19, 19))
    map[19][19] = "[ ]"
    map[0][0] = ["[A]"]
    
    awesome = pathfinder.Pathfinder()
    
    path = awesome.findShortestPath(ant, game)
    if not path:
        print "No path was found."
    for node in path:
        print "\n" * 50
        x, y = ant.loc
        map[x][y] = "[#]"
        x, y = node
        map[x][y] = "[A]"
        for row in map:
            print "".join(row)
        time.sleep(.25)


if __name__ == "__main__":
    for row in map:
        print "".join(row)
    run()
    for row in map:
        print "".join(row)
    
    
