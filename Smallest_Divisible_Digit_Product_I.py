class Solution:
    def digit(self, num: int) -> int:
        prod = 1
        for ch in str(num):
            prod *= int(ch)
        return prod

    def smallestNumber(self, n: int, t: int) -> int:
        num = n
        while self.digit(num) % t != 0:
            num += 1
        return num