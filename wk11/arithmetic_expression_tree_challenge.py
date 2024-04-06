
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def evaluate_expression_tree(root):
    # Your code here
    # Implement the postorder traversal to evaluate the expression represented by the tree.
    pass

# Example usage:
# Construct the expression tree for 3 + ((5*2) - (4/2))

# Nodes
node_plus = TreeNode('+')
node3 = TreeNode(3)
node_minus = TreeNode('-')
node_mult = TreeNode('*')
node5 = TreeNode(5)
node2_first = TreeNode(2)
node_div = TreeNode('/')
node4 = TreeNode(4)
node2_second = TreeNode(2)

# Construct the tree
node_plus.left = node3
node_plus.right = node_minus

node_minus.left = node_mult
node_minus.right = node_div

node_mult.left = node5
node_mult.right = node2_first

node_div.left = node4
node_div.right = node2_second

# root is the '+' node
root = node_plus

# The function call - You need to implement this function
result = evaluate_expression_tree(root)
print(result)  # Expected output: 11
