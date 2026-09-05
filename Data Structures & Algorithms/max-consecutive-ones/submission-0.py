class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutiveOneSum = 0
        largestSum = 0

        for i in nums:
            if i == 1:
                consecutiveOneSum += 1
                if consecutiveOneSum > largestSum:
                    largestSum = consecutiveOneSum
            else:
                consecutiveOneSum = 0
        return largestSum