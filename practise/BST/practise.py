def search_bst(root,target):
    if root is None:
        return None
    if root.val==target:
        return root
    if root.val>target:
        return search_bst(root.left,target)
    return search_bst(root.right,target)

def insertion_bst(root,node):
    if root is None:
        return TreeNode(node)
    if node<root.val:
        root.left=insertion_bst(root.left,node)
    else:
        root.right=insertion_bst(root.right,node)
    return root



def validateBst(root,low,high):
    if root is None:
        return None
    if root.value <=low or root.value>=high:
        return False
    return (validateBst(root.val,))