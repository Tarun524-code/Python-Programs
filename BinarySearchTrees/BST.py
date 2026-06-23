class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None


    def insert(self,node,data):
        if node is None:
            return Node(data)

        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        return node

    def delete(self,node, data):
        if node is None:
            return None

        if data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = self._find_min_node(node.right)
            node.data = successor.data
            node.right = self._delete_rec(node.right, successor.data)

        return node

    def _find_min_node(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def inOrder(self,root):
        if root is not None:
            self.inOrder(root.left)
            print(root.data,end = " ")
            self.inOrder(root.right)