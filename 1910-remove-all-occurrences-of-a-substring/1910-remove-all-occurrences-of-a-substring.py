class Solution(object):
    def removeOccurrences(self, s, part):
        index = s.find(part)
        if index == -1:
            return s
        else:
            s = s.replace(part, "", 1)
            return self.removeOccurrences(s, part)
