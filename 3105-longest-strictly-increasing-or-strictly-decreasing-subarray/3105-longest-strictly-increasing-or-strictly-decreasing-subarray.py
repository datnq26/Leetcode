class Solution(object):
    def longestMonotonicSubarray(self, nums):
        max_increase = 1
        max_decrease = 1
        
        count = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                count += 1
            else:
                count = 1
            if max_increase < count:
                max_increase = count
        
        count = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                count += 1
            else:
                count = 1
            if max_decrease < count:
                max_decrease = count
        
        if max_decrease > max_increase:
            return max_decrease
        return max_increase