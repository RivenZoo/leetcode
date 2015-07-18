#coding:utf-8

class Solution:
    reverse_bits = []
    def __init__(self):
        for i in range(256):
            r = 0
            for n in range(8):
                if i & (0x01<<n):
                    r |= (0x01<<(7-n))
            Solution.reverse_bits.append(r)

    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(4):
            result = (result << 8) | (Solution.reverse_bits[n & 0xff])
            n >>= 8
        return result

def main():
    s = Solution()
    print s.reverseBits(43261596)
    print s.reverseBits(0)
    print s.reverseBits(1)

if __name__ == '__main__':
    main()