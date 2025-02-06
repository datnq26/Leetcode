class Solution(object):
    def tupleSameProduct(self, nums):
        n = len(nums)
        
        hash_tb = dict()
        for i in range(n - 1):
            for j in range(i + 1, n):
                multi = nums[i] * nums[j]
                if hash_tb.get(multi):
                    hash_tb[multi].append((nums[i], nums[j]))
                else:
                    hash_tb[multi] = [(nums[i], nums[j])]
        
        number_of_pairs = 0
        for key, value in hash_tb.items():
            len_value = len(value)
            if len_value >= 2:
                number_of_pairs += self.factorial(len_value) / (self.factorial(len_value - 2) * 2)
        return int(number_of_pairs) * 8
    
    def factorial(self, n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res