
import time
from collections import namedtuple, OrderedDict
import math



Node = namedtuple("Node", ["loc", "parent", "g", "f"])


class EmptyNodeListError(Exception): pass


class Pathfinder():

    def addToHeap(self, node, heap):
        
        idx = len(heap) - 1
        while idx > 0:
            if node.f < heap[idx]:
                if node.f < heap[idx - 1]:
                    idx = math.floor(idx/2)            
                    continue
                else:
                    heap.insert(idx - 1, node)
            else:
                heap.insert(idx, node)

    def getAdjacentLocs(self, node):

        # loop over      north     east    south    west
        for direction in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            x, y = [x + y for x, y in zip(node.loc, direction)]
            yield (x, y)

    def constructPath(self, node, searched):

        print "Target destination reached"
        path = []
        while node.loc != node.parent:
            path.append(node.loc)
            node = searched[node.parent]
        print path
        return path

    def findShortestPath(self, ant, game):

        reachable_nodes = OrderedDict({tuple(ant.loc): Node(ant.loc, ant.loc, 0, 0)})
        searched_nodes = {}
        beginning = ant.loc
        end = ant.target

        while reachable_nodes:
            try:
                # This will get replaced with node scoring
                node_entry = sorted(reachable_nodes.iteritems())[0]
                reachable_nodes.pop(node_entry[0])
                current_node = node_entry[1]
            except IndexError:
                raise EmptyNodeListError
            if current_node.loc == end:
                return self.constructPath(current_node, searched_nodes)
            searched_nodes[current_node.loc] = current_node
            adjacent_locs = self.getAdjacentLocs(current_node)
            for loc in adjacent_locs:
                if loc not in reachable_nodes and loc not in searched_nodes:
                    if game.passable(loc):
                        # Get the distance from the parent for its G score
                        # TODO: This won't be perfect... make it perfect... someday
                        g = game.distance(loc, beginning)
                        # Get the F rating (total predicted path distance)
                        f = game.distance(loc, end) + g
                        node = Node(loc, current_node.loc, g, f)
                        reachable_nodes[loc] = node
        # For now, this means we're boxed in and the target was unreachable
        return None
            
    def findSafestPath(self, ant, game):
        
        pass
    
    def findMostVulnerablePath(self, ant, game):
        
        pass


# NOTE
# store shortest path
# If the path is interrupted just move into a clean node or don't move at all
# If forced to move find shortest path to next node in original path and resume tracking
