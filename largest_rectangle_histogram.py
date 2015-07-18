class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        # left bound index
        left_bound = [-1]
        largestArea = 0
        # left bound height, to pop all item
        height.append(0)
        for i, h in enumerate(height):
            while h < height[left_bound[-1]]:
                pos = left_bound.pop(-1)
                width = i - left_bound[-1] - 1
                rectArea = width * height[pos]
                largestArea = max(rectArea, largestArea)
            left_bound.append(i)
        return largestArea

def test_largest_rectarea():
    height = [2,1,5,6,2,3]
    s = Solution()
    print s.largestRectangleArea(height)

if __name__ == '__main__':
    test_largest_rectarea()