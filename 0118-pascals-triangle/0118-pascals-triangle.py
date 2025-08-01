class Solution(object):
    def generate(self, numRows):
        res = []
        for i in range(numRows):
            arr = []
            last_arr = []
            if len(res) > 0:
                last_arr = res[-1]

            res.append(arr)
            for j in range(i + 1):
                if j == i or j == 0:
                    arr.append(1)
                else:
                    arr.append(last_arr[j - 1] + last_arr[j])
        
        return res