#coding:utf8
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    def _trace_left(self, node):
        while node:
            self.trace.append(node)
            node = node.left

    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.trace = []
        self._trace_left(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if len(self.trace) == 0:
            return False
        return True

    # @return an integer, the next smallest number
    def next(self):
        l = len(self.trace)
        node = self.trace.pop(l-1)
        self._trace_left(node.right)
        return node.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

def build_bst():
    root = TreeNode(3)
    l1 = TreeNode(1)
    root.left = l1
    l2 = TreeNode(2)
    l1.right = l2
    r1 = TreeNode(4)
    root.right = r1
    return root

def test_bst_iterator():
    root = build_bst()
    itr = BSTIterator(root)
    while itr.hasNext():
        print itr.next()

if __name__ == '__main__':
    test_bst_iterator()