from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
#using recursion
    def max_depth_of_tree(self,root):
        if root is None:
            return -1
        return max(self.max_depth_of_tree(root.left),self.max_depth_of_tree(root.right))+1

    def max_depth_level(self,root):
        if root is None:
            return 0
        q=deque([root])
        depth=0
        while q:
            levelsize=len(q)
            for _ in range(levelsize):
                curr=q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            depth +=1
        return depth -1

    def min_depth(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return self.min_depth(root.right)+1
        if root.right is None:
            return self.min_depth(root.left)+1 
        return min(self.min_depth(root.left),self.min_depth(root.right))+1

    def min_depth_level(self,root):
        if not root:
            return 0
        q=deque([(root,1)])
        while q:
            node,depth=q.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append((node.left,depth+1))
            if node.right:
                q.append((node.right,depth+1))
        return depth
    
    def count_node(self,root):
        if root is None:
            return 0
        return 1+self.count_node(root.left)+self.count_node(root.right)

    def count_node_level(self,root):
        if root is None:
            return 0
        q=deque([root])
        count=0
        while q:
            curr=q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            count +=1
        return count

    def sum_node(self,root):
        if root is None:
            return 0
        left=self.sum_node(root.left)
        right=self.sum_node(root.right)
        return root.val + left + right

    def searchBT(self,root,target):
        if root is None:
            return False
        if root.val == target:
            return True
        return self.searchBT(root.left,target) or self.searchBT(root.right,target)

    def minDepth(self, root):
        if root is None:
            return 0
        q=deque([root])
        depth=1
        while q:
            curr=q.popleft()
            if not curr.left and not curr.right:
                return depth
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            depth +=1
        return depth
        
        
        


tree=BST()
tree.root=TreeNode(1)
tree.root.left=TreeNode(2)
tree.root.right=TreeNode(3)
tree.root.right.right=TreeNode(4)
tree.root.left.left=TreeNode(5)
tree.root.right.right.right=TreeNode(6)
tree.root.left.left.left=TreeNode(7)
# tree.<function_name(tree.root)>
# print(tree.max_depth_of_tree(tree.root))
# print(tree.max_depth_level(tree.root))
# print(tree.min_depth(tree.root))
# print(tree.min_depth_level(tree.root))
# print(tree.count_node_level(tree.root))
# print(tree.sum_node(tree.root))
# print(tree.searchBT(tree.root,5))

