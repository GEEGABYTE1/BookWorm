from data import*


class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.children = []

    def add_child(self, new_element):
        self.children.append(new_element)

    def remove_child(self, child_node):
        self.children = [i for i in self.children if not i == child_node]
    
    def traverse(self):
        nodes = [self]
        while len(nodes) > 0:
            current_node = nodes.pop()
            print(current_node.value)
            nodes += current_node.children


# Math Tree 
math_tree = TreeNode('Math')
for title, info in math.items():
    lst = [title, info]
    math_tree.add_child(TreeNode(lst))

# Computer Science Tree
com_sci_tree = TreeNode("Computer Science")
for title, info in com_sci.items():
    lst = [title, info]
    com_sci_tree.add_child(TreeNode(lst))

# Physics Tree
physics_tree = TreeNode("Physics")
for title, info in physics.items():
    lst = [title, info]
    physics_tree.add_child(TreeNode(lst))
