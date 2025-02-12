class Solution(object):
    def sum_element(self, num):
        sum = 0
        while num > 0:
            sum += num % 10
            num = num // 10
        return sum
    
    
    def maximumSum(self, nums):
        hash_tb = dict()
        for i in range(len(nums)):
            sum = self.sum_element(nums[i])
            if sum in hash_tb:
                hash_tb[sum].append(nums[i])
            else:
                hash_tb[sum] = [nums[i]]
        
        max_sum = -1
        for key, values in hash_tb.items():
            if len(values) > 1:
                max_value_1 = 0
                for i in range(len(values)):
                    if values[i] > max_value_1:
                        max_value_1 = values[i]
                
                values.remove(max_value_1)
                max_value_2 = 0
                for j in range(len(values)):
                    if values[j] > max_value_2:
                        max_value_2 = values[j]
                
                max_sum = max(max_sum, max_value_1 + max_value_2)
        return max_sum