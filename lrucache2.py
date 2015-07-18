#coding:utf8        
class LRUCache:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next, self.prev = None, None

    class Item:
        def __init__(self, node, value):
            self.node = node
            self.value = value

    def _init_visit_list(self):
        self.visit_list = LRUCache.Node(-1)
        self.visit_list.next = self.visit_list
        self.visit_list.prev = self.visit_list

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self._count = 0
        self._data = {}
        self._init_visit_list()

    def _lru_append(self, node):
        node.next = self.visit_list
        node.prev = self.visit_list.prev
        self.visit_list.prev = node
        node.prev.next = node

    def _lru_remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _update(self, node):
        self._lru_remove(node)
        self._lru_append(node)

    # @return an integer
    def get(self, key):
        item = self._data.get(key, None)
        if item:
            self._update(item.node)
            return item.value
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self._data.has_key(key):
            item = self._data[key]
            item.value = value
            self._update(item.node)
        else:
            node = LRUCache.Node(key)
            self._data[key] = LRUCache.Item(node, value)
            self._lru_append(node)
            self._count += 1
        
        node = self.visit_list.next
        while self._count > self.capacity and node != self.visit_list:
            self._lru_remove(node)
            self._data.pop(node.value)
            self._count -= 1
            node = node.next

    def trace(self):
        print '---------'
        node = self.visit_list.next
        while node != self.visit_list:
            print node.value,'->',
            node = node.next
        print '\n---------'

def test_lrucache():
    cache = LRUCache(2)
    cache.set(2, 1)
    cache.set(1, 1)
    cache.set(2, 3)
    cache.set(4, 1)
    cache.trace()
    print '1:', cache.get(1)
    print '2:', cache.get(2)

if __name__ == '__main__':
    test_lrucache()
