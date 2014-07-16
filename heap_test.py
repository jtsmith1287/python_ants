
from collections import namedtuple
import random
import time

class Pathfinder():

    def addToHeap(self, node, heap):
        
        idx = len(heap) - 1
        heap.append(node)
        if idx <= 1:
            return
        while idx >= 0:
            if idx == 0:
                return
            if heap[idx].f <= heap[int(idx/2)].f:
                parent_node = heap[int(idx/2)]
                heap[idx/2] = heap[idx]
                heap[idx] = parent_node
                idx = int(idx/2)
            else:
                return
    
    def removeTopNodeFromHeap(self, heap):
        
        top_node = heap.pop(0)
        while True:
            if len(heap) % 2: # Even number of nodes, meaning only one child exists
                pass
            else: # both child nodes exist
                pass
        
            

Node = namedtuple("Node", ["f"])
nodes = {}

for node in range(23):
    nodes[node] = Node(random.randint(1, 100))

for node in nodes:
    print node, nodes[node]

p = Pathfinder()
heap = []

for i in xrange(len(nodes)):
    p.addToHeap(nodes[i], heap)

for i in heap:
    print i
