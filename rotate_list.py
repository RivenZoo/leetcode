#coding:utf8

from data_struct import ListNode

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if not head:
            return head
            
        count = 0
        node, tail = head, head
        while node:
            count += 1
            tail = node
            node = node.next
        i = 0
        pos = count - k%count
        node = head
        while node:
            i += 1
            if i == pos:
                tail.next = head
                head = node.next
                node.next = None
            node = node.next
        return head

def test_rotate_right():
    head = ListNode.array2list([1,2,3,4])
    head.trace()
    head = Solution().rotateRight(head, 5)
    if head:
        head.trace()

if __name__ == '__main__':
    test_rotate_right()
                