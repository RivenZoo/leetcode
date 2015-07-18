#coding:utf-8

from data_struct import ListNode

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        if not node:
            return
        next = node.next
        while next:
            node.val = next.val
            if not next.next:
                node.next = None
                return
            node = next
            next = node.next

def main():
    head = ListNode.array2list([1,2,3,4])
    t = head.next
    Solution().deleteNode(t)
    head.trace()

if __name__ == '__main__':
    main()