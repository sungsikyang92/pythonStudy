class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # 전위순회
    def preorder(self, n):
        if n != None:
            print(n.value,' ', end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    # 중위순회
    def inorder(self, n):
        if n != None:
            if n.left:
                self.preorder(n.left)
            print(n.value,' ',end='')
            if n.right:
                self.preorder(n.right)

    # 후위순회
    def postorder(self, n):
        if n != None:
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)
            print(n.value,' ',end='')

    # 이진트리 높이
    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1