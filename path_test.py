
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
    if row < 0 or col < 0:
        print "Off the map... tisk tisk"
        return False
    try:
        if map[row][col] != "[W]":
            return True
    except IndexError:
        return False
    else:
        print "That's water... can't pass"
        return False

def run():
    Game = namedtuple("Game", ["distance", "passable"])
    Ant = namedtuple("Ant", ["loc", "target"])
    game = Game(distance, passable)
    ant = Ant((0, 10), (19, 19))
    map[0][10] = ["A"]
    
    awesome = pathfinder.Pathfinder()
    
    path = awesome.findShortestPath(ant, game)
    for node in path:
        x, y = ant.loc
        map[x][y] = "[#]"
        x, y = node
        map[x][y] = "[A]"
        for row in map:
            print "".join(row)
        time.sleep(2)


if __name__ == "__main__":
    run()
    for row in map:
        print "".join(row)
    
    