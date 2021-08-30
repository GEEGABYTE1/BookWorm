from Tree import TreeNode
from collections import deque 

def bfs(root_node, goal):
    path_queue = deque()
    initial_path = [root_node]
    path_queue.appendleft(initial_path)

    while path_queue:
        current_path = path_queue.pop()
        current_node = current_path[-1]
       #print("Searchin Book with title: {}".format(current_node.value[0]))
        if type(current_node.value) == list:
            titles = current_node.value 
            title = titles[0]
            if title == goal:
                return current_path 
            else:
                continue 
        else:
            for child in current_node.children:
                new_path = current_path[:]
                new_path.append(child)
                path_queue.appendleft(new_path)
    
    return None