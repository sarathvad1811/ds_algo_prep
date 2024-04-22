# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from collections import deque 
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def depth_binary_tree(root):
    if not root: return []
    
    left_subtree = depth_binary_tree(root.left)
    right_subtree = depth_binary_tree(root.right)
    
    return [root.value] + left_subtree + right_subtree
    
print(depth_binary_tree(root))


def breadth_binary_tree(root):
    if not root:
        return []
        
    q = deque()
    q.append(root)
    res = []
    
    while q:
        curr = q.popleft()
        res.append(curr.value)
        
        if curr.left: q.append(curr.left)
        if curr.left: q.append(curr.right)
        
    return res
    
print(breadth_binary_tree(root))


def tree_level_binary_tree(root):
    q, path = deque(), []
    
    if not root: return []
    
    q.append(root)
    
    while q:
        res = []
        for i in range(len(q)):
            curr = q.popleft()
            if curr.left: 
                q.append(curr.left)
            
            if curr.right: 
                q.append(curr.right)
        
            res.append(curr.value)
        
        path.append(res)
    
    return path
    
print(tree_level_binary_tree(root))

def tree_exists(root, node):
    if not root:
        return False
        
    if root.value == node:
        return True
    else:
        return tree_exists(root.left, node) or tree_exists(root.right, node)

print(tree_exists(root, 6))
print(tree_exists(root, 5))

def tree_sum_rec(root):
    if not root: return 0
    
    return root.value + tree_sum_rec(root.left) + tree_sum_rec(root.right)

print(tree_sum_rec(root))

def tree_sum_bfs(root):
    if not root: return 0
    
    q = deque()
    q.append(root)
    tree_sum = 0
    
    while q:
        curr = q.popleft()
        tree_sum += curr.value
        
        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)
    
    return tree_sum
        
print(tree_sum_bfs(root))

def min_num_tree(root):
    if not root: return float("inf")
        
    return min(root.value, min_num_tree(root.left), min_num_tree(root.right))
    
print(min_num_tree(root))

def max_path_sum(root):
    if not root: return float("-inf")
    if not root.left and not root.right: return root.value
    
    left_subtree_max = max_path_sum(root.left)
    right_subtree_max = max_path_sum(root.right)
    
    return root.value + max(left_subtree_max, right_subtree_max)

print(max_path_sum(root))
