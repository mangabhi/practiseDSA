class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


class BT:
    def __init__(self):
        self.root=None

    def lowest_common_acensotr(self,root,p,q):
        while root:
            if p.val<root.val and q.val<root.val:
                root=root.left
            elif p.val>root.val and q.val>root.val:
                root=root.right
            else:
                return root



tree=BT()
tree.root=TreeNode(1)
tree.root.left=TreeNode(2)
tree.root.right=TreeNode(3)
tree.root.left.left=TreeNode(4)
tree.root.left.right=TreeNode(5)

# tree.bfs(tree.root)
# print(tree.balance_BT(tree.root))
print(tree.lowest_common_acensotr(tree.root))