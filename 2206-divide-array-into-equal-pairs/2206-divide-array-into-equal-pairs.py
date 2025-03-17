class Solution(object):
    def divideArray(self, nums):
        hash_tb = dict()
        
        for i in range(len(nums)):
            if hash_tb.get(nums[i]):
                hash_tb[nums[i]] += 1
            else:
                hash_tb[nums[i]] = 1
        
        for key in hash_tb:
            if hash_tb[key] % 2 != 0:
                return False
        return True
    