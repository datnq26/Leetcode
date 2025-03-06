class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        leng = len(grid)
        hash_tb = dict()
        for i in range(leng):
            for j in range(leng):
                key = hash_tb.get(grid[i][j])
                if not key:
                    hash_tb[grid[i][j]] = 1
                else:
                    hash_tb[grid[i][j]] += 1
        
        missing = 0
        repeated = 0
        for i in range(1, leng * leng + 1):
            key = hash_tb.get(i)
            if not key:
                missing = i
            elif hash_tb[i] == 2:
                repeated = i
            
        return [repeated, missing]
            