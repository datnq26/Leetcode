class Solution(object):
    def twoSum(self, nums, target):
        leng = len(nums)
        for i in range(leng - 1):
            for j in range(i + 1, leng):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]
