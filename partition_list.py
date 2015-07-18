#coding:utf8

from data_struct import ListNode

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        less_head, less_tail = None, None
        gt_head, gt_tail = None, None
        node = head
        while node:
            if node.val < x:
                if not less_head:
                    less_head = node
                if less_tail:
                    less_tail.next = node
                less_tail = node
            else:
                if not gt_head:
                    gt_head = node
                if gt_tail:
                    gt_tail.next = node
                gt_tail = node
            node = node.next
        if less_tail:
            less_tail.next = gt_head
        if gt_tail:
            gt_tail.next = None
        return less_head if less_head else gt_head

def test_partition_list():
    head = ListNode.array2list([1,4,3,2,5,2])
    head.trace()
    s = Solution()
    ret = s.partition(None, 0)
    if ret:
        ret.trace()

if __name__ == '__main__':
    test_partition_list()


