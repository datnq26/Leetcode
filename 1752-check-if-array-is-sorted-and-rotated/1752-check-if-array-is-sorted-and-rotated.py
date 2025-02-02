import copy

class Solution(object):
    def check(self, nums):
        arr = copy.deepcopy(nums)
        sorted_arr = sorted(arr)
        
        n = len(nums)
        possible_shifts = [i for i in range(n) if nums[i] == sorted_arr[0]]

        for x in possible_shifts:
            if all(sorted_arr[i] == nums[(i + x) % n] for i in range(n)):
                return True
        
        return False