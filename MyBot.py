#!/usr/bin/env python
from ants import *
from pathfinder import Pathfinder
import random

ATTACK = 0
GATHER = 1
LEAD = 2
EXPLORE = 3

######################### AI Execution Order ###########################
# Determine Priority
# Determine shortest path
# Execute
# Redertimine priority defaulting to existing priority
########################################################################


class IndividualAnt():

    max_id = 0
    
    def __init__(self, loc):

        self.loc = loc
        self.target = None
        self.alive = True
        self.priority = EXPLORE
        self.goal_met = False
        self.uid = -1

    def assignUID(self):

        self.uid = self.max_id + 1
        self.max_id += 1


class MyBot:

    def __init__(self):

        self.ants_dict = {}
        self.pending_moves= []
        self.game = None
        self.actions = {3: self.explore}
        self.pathfinder = Pathfinder()

    def do_setup(self, ants):
        pass

    def getAnt(self, loc, loc_list):
        """Returns new ant if it exists else a new ant."""

        if loc not in loc_list:
            ant = IndividualAnt(loc)
            self.ants_dict[loc] = ant
        else:
            ant = self.ants_dict[loc]
        return ant        

    def assignPriority(self, ant):

        pass

    def explore(self, ant):

        if not ant.target:
            ant.target = (random.choice(range(self.game.map[0])),
                          random.choice(range(self.game.map[1])))
            if not self.game.passable(ant.target):
                ant.target = None
                self.explore(ant)
                return            
                

    def startPriorityAction(self, ant):

        if ant.goal_met:
            pass # TODO: determine next priority
        else:
            self.actions[ant.priority](ant)

    def updateAntData(self, ant, new_loc):

        self.pending_moves.append(new_loc)
        self.ants_dict[new_loc] = self.ants_dict.pop(ant.loc)
        ant.loc = new_loc

    def determineNextMove(self, ant, direction):

        new_loc = self.game.destination(ant.loc, direction)
        if (self.game.passable(new_loc)) and (
                new_loc not in self.pending_moves):
            self.game.issue_order((ant.loc, direction))
            self.updateAntData(ant, new_loc)
            return True

    def do_turn(self, ants):

        self.pending_moves = []
        if not self.game:
            self.game = ants
        loc_list = self.ants_dict.keys() # This sucks
        for loc in self.game.my_ants():
            ant = self.getAnt(loc, loc_list)
            directions = ('n','e','s','w')
            for direction in directions:
                new_loc = self.determineNextMove(ant, direction)
                if new_loc:
                    break
            if self.game.time_remaining() < 10:
                break
            
if __name__ == '__main__':
    # psyco will speed up python a little, but is not needed
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass
    
    try:
        # if run is passed a class with a do_turn method, it will do the work
        # this is not needed, in which case you will need to write your own
        # parsing function and your own game state class
        Ants.run(MyBot())
    except KeyboardInterrupt:
        print('ctrl-c, leaving ...')

