class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    def insert(self,root,value):
        if root is None:
            return TreeNode(value)
        if value < root.val:
            root.left=self.insert(root.left,value)
        else:
            root.right=self.insert(root.right,value)
        return root

    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.val,end=" ")
        self.inorder(root.right)

    def search(self,root,value):
        if root is None:
            return False
        if value == root.val:
            return True
        if value < root.val:
            return self.search(root.left,value)
        else:
            return self.search(root.right,value)

    def isValidate(self,root):
        def dfs(root,low,high):
            if root is None:
                return True
            if root.val <=low or root.val >= high:
                return False
            return (dfs(root.left,low,root.val) and dfs(root.right,root.val,high))
        return dfs(root,float('-inf'),float('inf'))

    def mimimum_val_bst(self,root):
        if root is None:
            return -1
        while root.left:
            root=root.left
        return root.val

    def mamximum_val_bst(self,root):
        if root is None:
            return -1
        while root.right:
            root=root.right
        return root.val

    def kth_smallest(self,root,k):
        n=0
        stack=[]
        curr=root 

        while curr and stack:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            n+=1
            if n==k:
                return curr.val
            curr=curr.right
            


        
        
        




tree=BST()
tree.root = TreeNode(15)

tree.root.left = TreeNode(10)
tree.root.right = TreeNode(20)

tree.root.left.left = TreeNode(8)
tree.root.left.right = TreeNode(12)

tree.root.right.left = TreeNode(17)
tree.root.right.right = TreeNode(25)

tree.root.left.left.left = TreeNode(6)
tree.root.left.left.right = TreeNode(9)

# tree.insert(tree.root,50)
# print(tree.inorder(tree.root))
# print(tree.inorder(tree.root),end=" ")
# print(tree.search(tree.root,7))
# print(tree.isValidate(tree.root))
print(tree.mimimum_val_bst(tree.root))
print(tree.mamximum_val_bst(tree.root))