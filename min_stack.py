#coding:utf-8

class MinStack:
    def __init__(self):
        self._stack = []
        self._min = []

    def _push_min(self, x):
        if len(self._min) == 0:
            self._min.append(x)
            return
        top = self._min[-1]
        if x > top:
            return
        self._min.append(x)

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self._stack.append(x)
        self._push_min(x)
        return x

    # @return nothing
    def pop(self):
        top = self._stack.pop()
        if top == self._min[-1]:
            self._min.pop()

    # @return an integer
    def top(self):
        return self._stack[-1]

    # @return an integer
    def getMin(self):
        return self._min[-1]