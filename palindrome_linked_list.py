#coding:utf-8

from data_struct import ListNode

class Solution:
    @staticmethod
    def _find_middle(head):
        'return mid(odd)/mid+1(even)'
        slow = head
        fast = head
        while fast:
            if not fast.next:
                break
            slow = slow.next
            fast = fast.next.next
        return slow

    @staticmethod
    def _reverse(head):
        'return reversed_head'
        if not head:
            return head
        p = head.next
        head.next = None
        while p:
            tmp = p.next
            p.next = head
            head = p
            p = tmp
        return head

    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        mid = Solution._find_middle(head)
        right = Solution._reverse(mid)
        left = head
        palindrome = False
        p = right
        while p:
            if left.val != p.val:
                break
            left = left.next
            p = p.next
        if not p:
            palindrome = True
        right = Solution._reverse(right)
        return palindrome

    @staticmethod
    def _palindirome_cmp(head):
        'this is a wrong answer'
        'use recursion stack to store node, not accepted cause stack overflow'
        if not head:
            return False

        _cur = [head]
        right = head.next
        def _inner_check(right):
            if not right:
                return True
            if not _inner_check(right.next):
                return False
            node = _cur[0]
            if node.val == right.val:
                _cur[0] = node.next
                return True
            return False
        return _inner_check(right)
        
def main():
    head = ListNode.array2list([1,2,2,1,1])
    print Solution().isPalindrome(head)
    head.trace()
    print Solution()._find_middle(head)
    h = Solution._reverse(ListNode.array2list([1,2,3,4,5]))
    h.trace()

if __name__ == '__main__':
    main()