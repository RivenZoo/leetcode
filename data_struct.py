#coding:utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __unicode__(self):
        return u'val:%s'%(self.val,)
    def __str__(self):
        return self.__unicode__().encode('utf-8')
    @staticmethod
    def array2list(a):
        head, tail = None, None
        for i in a:
            if not head:
                head = ListNode(i)
                tail = head
            else:
                node = ListNode(i)
                tail.next = node
                tail = node
        return head

    def trace(self):
        node = self
        while node:
            print node.val,'->',
            node = node.next
        print 'end'