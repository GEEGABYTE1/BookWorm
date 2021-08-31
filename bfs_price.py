from collections import deque 
from Tree import TreeNode 

def bfs_price(root_node, goal):
    path_queue = deque()
    initial_path = [root_node]
    path_queue.appendleft(initial_path)
    while path_queue:
        current_path = path_queue.pop()
        current_node = current_path[-1]
        if type(current_node.value) == str:
            pass 
        else:
            if current_node.value[0] == goal:
                return current_path 
    
        for child in current_node.children:
            new_path = current_path[:]
            new_path.append(child)
            path_queue.appendleft(new_path)
    
    return None