class Solution(object):
    def countOfSubstrings(self, word, k):
        length = 5 + k
        word_arr = list(word)

        count = 0
        for i in range(len(word_arr) - 1):
            for j in range(i + 1, len(word_arr) + 1):
                if len(word_arr[i:j]) < length:
                    continue
                if self.checkValid(''.join(word_arr[i:j]), k):
                    count += 1
        return count
            
    def checkValid(self, word, k):
        arr = list(word)
        if not ('a' in arr and 'e' in arr and 'i' in arr and 'o' in arr and 'u' in arr):
            return False
        
        non_vowels = list()
        for i in range(len(arr)):
            if arr[i] != 'a' and arr[i] != 'e' and arr[i] != 'i' and arr[i] != 'o' and arr[i] != 'u':
                non_vowels.append(arr[i])
        
        count = len(non_vowels)
        if count != k:
            return False
        
        return True
        
sol = Solution()
print(sol.countOfSubstrings("iqeaouqi", 2))