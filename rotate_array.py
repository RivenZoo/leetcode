#coding:utf-8

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate2(self, nums, k):
        size = len(nums)
        if not size: return

        if size < k:
            k %= size
        next = 0
        start = size - k
        tmp = nums[start]
        while next != start:
            nums[next], tmp = tmp, nums[next]
            next = (next + k)%size
        nums[start] = tmp
    
    @staticmethod
    def rotateAll(arr, start, n):
        for i in range(n/2):
            arr[start+i], arr[start+n-1-i] = arr[start+n-1-i], arr[start+i]

    def rotate(self, nums, k):
        '''rotate to right by k steps lead to right k elements moved to left
           nums:[a|b] rotate k steps => [b'|a'], len(b)==k
           rotate nums => rotate([a|b]) => rotate(rotate(a)|rotate(b))
        '''
        size = len(nums)
        if not size: return

        if size < k:
            k %= size
        Solution.rotateAll(nums, 0, size-k)
        Solution.rotateAll(nums, size-k, k)
        Solution.rotateAll(nums, 0, size)

def parray(a):
    for i in a:
        print i,
    print ''

def test(case, fn, *args):
    map(lambda x: fn(x, *args), case)
    map(lambda x: parray(x), case)

def main():
    case = [[1,2,3,4,5,6,7]]
    s = Solution()
    test(case, s.rotateAll, 0, 3)

    case = [[1,2,3,4,5,6,7],[1,2,3],[]]
    test(case, s.rotate, 4)

    case = [[1,2,3,4,5,6,7],[1,2,3],[]]
    test(case, s.rotate2, 4)

if __name__ == '__main__':
    main()