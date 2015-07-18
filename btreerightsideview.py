# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        if not root:
            return []
        odd_level = []
        even_level = []
        result = []
        odd_level.append(root)
        cur = odd_level
        next = even_level
        while len(cur) != 0:
            node = cur.pop(0)
            if node.left:
                next.append(node.left)
            if node.right:
                next.append(node.right)
            if len(cur) == 0:
                result.append(node.val)
                if cur == odd_level:
                    cur = even_level
                    next = odd_level
                else:
                    cur = odd_level
                    next = even_level
        return result

def build_tree():
    root = TreeNode(1)
    l1 = TreeNode(2)
    l2 = TreeNode(5)
    root.left = l1
    l1.right = l2
    r1 = TreeNode(3)
    root.right = r1
    r2 = TreeNode(4)
    r1.right = r2
    return root

def test_right_side_view():
    root = build_tree()
    s = Solution()
    print s.rightSideView(root)

if __name__ == '__main__':
    test_right_side_view()