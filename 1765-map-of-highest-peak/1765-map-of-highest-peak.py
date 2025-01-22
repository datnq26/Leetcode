class Solution(object):
    def calculation(self, result):
        for i in range(len(result)):
            for j in range(len(result[i])):
                if result[i][j] != 1:
                    arr = []
                    if i > 0:
                        if result[i-1][j] != 0:
                            arr.append(result[i-1][j])
                    if i < len(result)-1:
                        if result[i+1][j] != 0:
                            arr.append(result[i+1][j])
                    if j > 0:
                        if result[i][j-1] != 0:
                            arr.append(result[i][j-1])
                    if j < len(result[i])-1:
                        if result[i][j+1] != 0:
                            arr.append(result[i][j+1])
                    if arr:
                        result[i][j] = min(arr) + 1
        return result
                        
    def highestPeak(self, isWater):
        m = len(isWater)
        n = len(isWater[0])
        result = [[0 for i in range(n)] for j in range(m)]
        for i in range(len(isWater)):
            for j in range(len(isWater[i])):
                if isWater[i][j] == 1:
                    result[i][j] = 0
                    if i > 0:
                        result[i-1][j] = 1
                    if i < len(isWater)-1:
                        result[i + 1][j] = 1
                    if j > 0:
                        result[i][j-1] = 1
                    if j < len(isWater[i])-1:   
                        result[i][j+1] = 1
        self.calculation(result)
        for i in range(len(isWater)):
            for j in range(len(isWater[i])):
                if isWater[i][j] == 1:
                    result[i][j] = 0
        return result