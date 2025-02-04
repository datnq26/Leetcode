class Solution(object):
    def maxAscendingSum(self, nums):
        n = len(nums)
        max_sum = nums[0]
        arr_sum = nums[0]
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                arr_sum = arr_sum + nums[i + 1]
            else:
                arr_sum = nums[i + 1]
            
            if max_sum < arr_sum:
                max_sum = arr_sum
        return max_sum