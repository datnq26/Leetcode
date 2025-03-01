class Solution(object):
    def applyOperations(self, nums):
        leng = len(nums)
        for i in range(leng - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        for i in range(leng):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
        return nums