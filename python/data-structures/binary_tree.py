class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.data:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print (root.data)
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print (root.data)
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print (root.data)

def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.data))
        printTree(node.right, level + 1)

# Example usage:
root = None
values = [5, 3, 7, 2, 4, 6, 8]

for value in values:
    root = insert(root, value)
print ("preorder_traversal\n")
preorder_traversal(root)
print ("\nInorder_traversal\n")
inorder_traversal(root)
print ("\nPostorder_traversal\n")
postorder_traversal(root)
printTree(root)