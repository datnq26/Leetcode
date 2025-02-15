class Solution(object):
    def can_partition(self, num_str, target, index=0, current_sum=0):
        if index == len(num_str):
            return current_sum == target

        temp = 0
        for j in range(index, len(num_str)):
            temp = temp * 10 + int(num_str[j])
            if current_sum + temp > target:
                break
            if self.can_partition(num_str, target, j + 1, current_sum + temp):
                return True
        return False

    def punishmentNumber(self, n):
        total = 0
        for i in range(1, n + 1):
            squared = str(i * i)
            if self.can_partition(squared, i):
                total += i * i
        return total
