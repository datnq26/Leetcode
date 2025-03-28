class Solution(object):
    def longestSquareStreak(self, nums):
        nums = set(nums)
                
        hash_tb = dict()
        for num in nums:
            hash_tb[num] = []
            check = num
            while check in nums:
                hash_tb[num].append(check)
                check = check * check
        
        max_result = 0
        for num in nums:
            max_result = max(max_result, len(hash_tb[num]))
            
        if max_result == 1:
            return -1
        
        return max_result