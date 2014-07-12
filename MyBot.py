#!/usr/bin/env python
from ants import *


HUNTER = 0
GATHERER = 1
LEADER = 2
EXPLORER = 3


class IndividualAnt():

    max_id = 0
    
    def __init__(self, loc):
        self.loc = loc
        self.alive = True
        self.state = EXPLORER
        self.uid = -1

    def assignUID(self):
        self.uid = self.max_id + 1
        self.max_id += 1


class MyBot:

    def __init__(self):

        self.ants_dict = {}
        self.pending_moves= []
        self.game = None

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

    def assignJob(self, ant):

        pass

    def updateAntData(ant, new_loc):

        self.pending_moves.append(new_loc)
        self.ants_dict[new_loc] = self.ants_dict.pop(ant.loc)
        ant.loc = new_loc

    def determineNextMove(self, ant, direction):

        new_loc = self.game.destination(ant.loc, direction)
        if (self.game.passable(new_loc)) and (
                new_loc not in self.pending_moves):
            self.game.issue_order((ant.loc, direction))
            return True

    def do_turn(self, ants):

        self.pending_moves = []
        self.game = ants
        loc_list = self.ants_dict.iterkeys()
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

