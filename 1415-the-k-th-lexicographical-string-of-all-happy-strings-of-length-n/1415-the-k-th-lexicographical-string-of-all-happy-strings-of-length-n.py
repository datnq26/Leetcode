class Solution(object):
    def getHappyString(self, n, k):
        happy_strs = []
        self.backtracking("", n, happy_strs)
        if k > len(happy_strs):
            return ""
        return happy_strs[k - 1]
    
    def backtracking(self, curr, n, happy_strs):
        if len(curr) == n:
            happy_strs.append(curr)
            return
        
        for ch in "abc":
            if not curr or curr[-1] != ch: 
                self.backtracking(curr + ch, n, happy_strs)