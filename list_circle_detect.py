#coding:utf8

from data_struct import ListNode

#---a-------|
#     |--b--|
#(a+b)/1=(a+b+k*c)/2
#a+b=k*c

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            # circle exist
            if fast == slow:
                break
        # circle exist, reset slow, fast use speed=1
        slow = head
        while fast:
            if fast == slow:
                return fast
            fast = fast.next
            slow = slow.next
        return None

def test_circle_detect():
    head = ListNode.array2list([1,2,3,4])
    node = head
    while node:
        if not node.next:
            break
        node = node.next
    node.next = head
    ret = Solution().detectCycle(head)
    if ret:
        print ret.val

if __name__ == '__main__':
    test_circle_detect()
