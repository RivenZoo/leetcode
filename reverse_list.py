#coding:utf8

from data_struct import ListNode

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head or not head.next:
            return head
        
        new_head = head
        node = head.next
        head.next = None
        
        while node:
            tmp = node.next
            node.next = new_head
            new_head = node
            node = tmp
        return new_head
        
def test_reverse_list():
    head = ListNode.array2list([1,2,3,])
    head.trace()
    head = Solution().reverseList(None)
    if head:
        head.trace()

if __name__ == '__main__':
    test_reverse_list()