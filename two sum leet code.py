class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = 1
        for i in range(len(nums)):
            for j in range(x ,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    break
            x =  x + 1