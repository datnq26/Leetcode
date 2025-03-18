class Solution(object):
    def longestNiceSubarray(self, nums):
        start = 0
        used_bits = 0
        max_length = 0

        for end in range(len(nums)):
            while (used_bits & nums[end]) != 0:
                used_bits ^= nums[start]
                start += 1
            
            used_bits |= nums[end]
            max_length = max(max_length, end - start + 1)

        return max_length

sol = Solution()
print(sol.longestNiceSubarray([1,3,8,48,10]))  # Kết quả: 3
