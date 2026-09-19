from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val=val 
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None

    def preorder(self,root):
        if root is None:
            return
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

    def postorder(self,root):
        if root is None:
            return 
        self.postorder(root.right)
        self.postorder(root.left)
        print(root.val)
#Zigzag Level Order Traversal
    def zizag_traversal(self,root):
        if root is None:
            return 
        res=[]
        q=deque([root])
        left_to_right=True
        while q:
            level=deque()
            for _ in range(len(q)):
                curr=q.popleft()
                if left_to_right:
                    level.append(curr.val)
                else:
                    level.appendleft(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(list(level))
            left_to_right=not left_to_right
        return res

    def right_view(self,root,level,maxlevel,res):
        if root is None:
            return 
        if level >maxlevel[0]:
            res.append(root.val)
            maxlevel[0]=level
        self.right_view(root.right,level+1,maxlevel,res)
        self.right_view(root.left,level+1,maxlevel,res)

    def right_view_dfs(self,root):
        res=[]
        maxLevel=[-1]
        self.right_view(root,0,maxLevel,res)
        return res

    def right_side_bfs(self,root):
        if root is None:
            return []
        res=[]
        q=deque([root])
        while q:
            level_size=len(q)
            for i in range(level_size):
                curr=q.popleft()
                if i==level_size-1:
                    res.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return res
# Left Side View
    def left_side_bfs(self,root):
        if root is None:
            return []
        res=[]
        q=deque([root])
        while q:
            level_size=len(q)
            for i in range(level_size):
                curr=q.popleft()
                if i==0:
                    res.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return res
#normal traversal
    def bfs_traversal(self,root):
        if root is None:
            return []
        q=deque([root])
        res=[]
        while q:
            curr=q.popleft()
            res.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return res

    def bfs_traversal_depth(self,root):
        if root is None:
            return 
        q=deque([root])
        depth=0
        while q:
            level_size=len(q)
            for _ in range(level_size):
                curr=q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            depth +=1
        return depth
    
    def bfs_traversal_array(self,root):
            if root is None:
                return 
            q=deque([root])
            res=[]
            while q:
                level_arr=[]
                level_size=len(q)
                for _ in range(level_size):
                    curr=q.popleft()
                    level_arr.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                res.append(level_arr)
            return res
        

# Create Binary Tree
tree = BinaryTree()

tree.root = TreeNode(1)

tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)

tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)

tree.root.right.left = TreeNode(6)
tree.root.right.right = TreeNode(7)
# tree.preorder(tree.root)

# print("Inorder")
# tree.inorder(tree.root)
# print("----------------------------------")
# tree.postorder(tree.root)
# print(tree.zizag_traversal(tree.root))
# print(tree.right_view_dfs(tree.root))
# print(tree.right_side_bfs(tree.root))
# print(tree.left_side_bfs(tree.root))
print(tree.bfs_traversal_array(tree.root))