class Solution(object):
    def mergeAlternately(self, word1, word2):        
        arr1 = list(word1)
        arr2 = list(word2)

        hash_tb = dict()
        
        for i in range(len(arr1)):
            hash_tb[i] = [arr1[i]]
            
        for i in range(len(arr2)):
            if hash_tb.get(i):
                hash_tb[i].append(arr2[i])
            else:
                hash_tb[i] = arr2[i]
                
        result = []
        
        for value in hash_tb.values():
            for num in value:
                result.append(num)
        
        return ''.join(result)
    
sol = Solution()
print(sol.mergeAlternately("abc", "pqrc"))