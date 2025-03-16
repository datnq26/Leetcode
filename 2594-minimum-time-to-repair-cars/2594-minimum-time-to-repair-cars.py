class Solution(object):
    def repairCars(self, ranks, cars):
        max_time = max(ranks) * cars * cars
        min_time = 0
        
        mid_time = (max_time + min_time) // 2
        while max_time - min_time > 1:
            count = 0
            for rank in ranks:
                count += int((mid_time / rank) ** 0.5)
            
            if count >= cars:
                max_time = mid_time
            else:
                min_time = mid_time
            mid_time = (max_time + min_time) // 2
        return max_time