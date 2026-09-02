"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # do bfs to get a deep copy

        #check if graph exists
        if not node:
            return None
        
        newgraph = {}
        newgraph[node] = Node(node.val)
        # initialise queue with root
        q = deque([node])

        # while we still have levels to visit
        while q:
            current_node = q.popleft()
            for neighbour in current_node.neighbors:
                if neighbour not in newgraph:
                    newgraph[neighbour] = Node(neighbour.val)
                    q.append(neighbour)
                newgraph[current_node].neighbors.append(newgraph[neighbour])
            
        return newgraph[node]
