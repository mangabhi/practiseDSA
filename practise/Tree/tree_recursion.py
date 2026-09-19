from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def preorder(self,root):
        if root is None:
            return 
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def bfs(self,root):
        if root is None:
            return 
        q=deque([root])
        while q:
            curr=q.popleft()
            print(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        
#Balanced Binary Tree
    def balance_BT(self,root):
        def getHeight(root):
            if root is None:
                return 0
            return 1+max(getHeight(root.left),getHeight(root.right))
        if root is None:
            return []
        lHeight=getHeight(root.left)
        rHeight=getHeight(root.right)

        if abs(lHeight- rHeight) > 1:
            return False
        return (self.balance_BT(self.left)and self.balance_BT(self.right))

    def balance_BT_optimise(self,root):
        if root is None:
            return 0
        lHeight=self.balance_BT_optimise(root.left)
        rHeight=self.balance_BT_optimise(root.right)

        if lHeight ==-1 or rHeight ==-1 or abs(lHeight-rHeight)>1:
            return -1
        return max(lHeight,rHeight)+1

    def balance_BS_tree(self,root):
        return self.balance_BT_optimise(root) !=-1

    def diameter_BS(self,root):
        def height(root):
            if root is None:
                return 0
            return 1+max(height(root.left),height(root.right))
        if root is None:
            return 0
        lheight=height(root.left)
        rheight=height(root.right)

        ldaimeter=self.diameter_BS(root.left)
        rdaimeter=self.diameter_BS(root.right)
        return max(lheight+rheight,ldaimeter,rdaimeter)

    def daimeter_BT(self,root):
        diameter=0
        def height(root):
            nonlocal diameter
            if root is None:
                return 0
            left=height(root.left)
            right=height(root.right)
            diameter =max(diameter,left+right)
            return 1+max(left,right)
        height(root)
        return diameter

    def maximum_sum_bT(self,root):
        max_sum=float('-inf')
        def dfs(root):
            nonlocal max_sum
            if root is None:
                return 0
            left=max(0,dfs(root.left))
            right=max(0,dfs(root.right))
            max_sum=max(max_sum,root.val+left+right)
            return root.val+max(left,right)
        dfs(root)
        return max_sum
        
    def path_sum(self,root,target=8):
        if root is None:
            return False
        target -=root.val
        if root.left is None and root.right is None:
            return target ==0 
        return(self.path_sum(root.left,target)or self.path_sum(root.right,target))

    def pathSum2(self, root, targetSum=8):
        res=[]
        def sumPath(root,target,path):
            if root is None:
                return 
            path.append(root.val)
            target -=root.val
            if root.left is None and root.right is None:
                if target == 0:
                    res.append(path[:])
            else: 
                sumPath(root.left,target,path)  
                sumPath(root.right,target,path)
            path.pop()
        sumPath(root,targetSum,[])
        return res

tree=BST()
tree.root=TreeNode(1)
tree.root.left=TreeNode(2)
tree.root.right=TreeNode(3)
tree.root.left.left=TreeNode(4)
tree.root.left.right=TreeNode(5)

# tree.bfs(tree.root)
# print(tree.balance_BT(tree.root))
print(tree.pathSum2(tree.root))