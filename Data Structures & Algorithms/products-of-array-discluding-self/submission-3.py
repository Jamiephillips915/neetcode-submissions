class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        index = 0
        total = [nums[_] for _ in range(len(nums)) if nums[_] != 0]
        num = 1
        for i in range(len(total)):
            num = num * total[i]
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
                index = i
        if zeros > 1:
            return [0 for _ in range(len(nums))]
        elif zeros == 1:
            return [0 if _ != index else num for _ in range(len(nums))]
        else:
            return [num // nums[i] for i in range(len(nums))]