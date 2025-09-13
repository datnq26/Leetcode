class Solution(object):
    def maxFreqSum(self, s):
        hash_tb = dict()
        for val in s:
            if hash_tb.get(val) is not None:
                hash_tb[val] += 1
            else:
                hash_tb[val] = 1
        vowels = [u'a', u'i', u'u', u'e', u'o']
        max_vowels = 0
        max_consonants = 0

        for key, val in hash_tb.items():
            if key in vowels:
                if max_vowels <= val:
                    max_vowels = val
            else:
                if max_consonants <= val:
                    max_consonants = val
        
        return max_vowels + max_consonants