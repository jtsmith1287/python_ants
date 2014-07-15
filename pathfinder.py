
LOC = 0
PARENT = 1
SCORE_G = 2

class Pathfinder():

    def getBestNode(self, open_nodes, f_scores):
        
        if f_scores:
            idx = f_scores.index(min(f_scores))
        else:
            idx = 0
        return open_nodes.pop(idx)

    def findShortestPath(self, ant, game):
        
        # Start and end locations
        beginning = [list(ant.loc), list(ant.loc), 0]
        end = list(ant.target)
        # Node data tracking
        open_nodes = []
        closed_nodes = []
        f_scores = []
        checked_nodes = 0
        # Set starting node
        open_nodes.append(beginning)
        
        # Begin loop... here we go
        while open_nodes:
            checked_nodes += 1
            current_node = self.getBestNode(open_nodes, f_scores)
            current_loc = current_node[LOC]
            if current_loc not in closed_nodes:
                closed_nodes.append(current_loc)
            # loop over      north     east    south    west
            for direction in ((0, -1), (0, 1), (1, 0), (0, -1)):
                # Get the actual map coordinates of the direction
                possible_loc = [x + y for x, y in zip(current_loc, direction)]
                if possible_loc == end:
                    closed_nodes.append(possible_loc)
                    return closed_nodes
                if game.passable(possible_loc) and possible_loc not in closed_nodes:
                    if possible_loc not in open_nodes:
                        f = game.distance(current_loc, possible_loc) + checked_nodes
                        #               Location      Parent       G score        F score
                        open_nodes.append([possible_loc, current_loc, checked_nodes])
                        f_scores.append(f)
            
            
    def findSafestPath(self, ant, game):
        
        pass
    
    def findMostVulnerablePath(self, ant, game):
        
        pass


# NOTE
# store shortest path
# If the path is interrupted just move into a clean node or don't move at all
# If forced to move find shortest path to next node in original path and resume tracking