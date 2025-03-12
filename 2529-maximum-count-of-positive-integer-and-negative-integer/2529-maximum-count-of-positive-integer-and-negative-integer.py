class Solution(object):
    def maximumCount(self, nums):
        max_pos = 0
        max_neg = 0
        
        for i in nums:
            if i > 0:
                max_pos += 1
            if i < 0:
                max_neg += 1
        
        return max_pos if max_pos > max_neg else max_neg
        