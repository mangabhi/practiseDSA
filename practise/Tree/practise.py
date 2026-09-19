from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def isBalanced(self,root):
        def dfs(root):
            if root is None:
                return True
            left,right=dfs(root.left),dfs(root.right)
            if abs(left-right)>1 or left == -1 or right ==-1 :
                return -1
            return 1+max(left,right)
        return dfs(root) != -1

    def good_node(self,root):
        def dfs(root,maxVal):
            if not root:
                return 0
            maxVal=max(maxVal,root.val)
            res=1 if root.val >= maxVal else 0
            res +=dfs(root.left,maxVal)
            res +=dfs(root.right,maxVal)
            return res 
        return dfs(root,root.val)

    def invert_tree(self,root):
        # def dfs(root):
        #     if root is None:
        #         return 
        #     left=dfs(root.left)
        #     right=dfs(root.right)
        #     #swap node
        #     root.left=right
        #     root.right=left
        #     return root
        # return dfs(root)
        if root is None:
            return None
        root.left,root.right=root.right,root.left
        self.invert_tree(root.left)
        self.invert_tree(root.right)
        return root

    def merge_2_bt(self,t1:TreeNode,t2:TreeNode)->TreeNode:
        if not t1 and t2:
            return None
        # valu1=t1.val if t1 else 0
        # valu2=t2.val if t2 else 0
        # root = TreeNode(valu1+valu2)
        # self.merge_2_bt(t1.left,t2.left)
        # self.merge_2_bt(t1.right,t2.right)
        # return root

        t1.val=t1.val+t2.val 
        t1.left=self.merge_2_bt(t1.left,t2.left)
        t1.right=self.merge_2_bt(t1.right,t2.right)
        return t1

    def sorted_array_bt(self,nums):
        def dfs(low,high):
            if low>high:
                return None
            mid=(low+high)//2
            root=TreeNode(nums[mid])
            root.left=dfs(low,mid-1)
            root.right=dfs(mid+1,high)
            return root
        return dfs(0,len(nums)-1)

    def isValidate(self,root):
        def dfs(root,low,high):
            if root is None:
                return True
            if root.val <=low or root.val >= high:
                return False
            return (dfs(root.left,low,root.val) and dfs(root.right,root.val,high))
        return dfs(root,float('-inf'),float('inf'))
    

            

tree=BST()
tree.root=TreeNode(1)
tree.root.left=TreeNode(2)
tree.root.right=TreeNode(3)
tree.root.left.left=TreeNode(4)
tree.root.left.right=TreeNode(5)

# tree.bfs(tree.root)
# print(tree.isBalanced(tree.root))
# print(tree.good_node(tree.root))
# print(tree.pathSum2(tree.root))
# print(tree.invert_tree(tree.root))
print(tree.merge_2_bt(tree.root,tree.root))