class Solution(object):
    def areAlmostEqual(self, s1, s2):
        if s1 == s2:
            return True
        
        len_s1 = len(s1)
        len_s2 = len(s2)
        list_s1 = list(s1)
        list_s2 = list(s2)
        
        if len_s1 != len_s2:
            return False
        
        diff_list = []
        for i in range(len(s1)):
            if list_s1[i] != list_s2[i]:
                diff_list.append(i)

        if len(diff_list) != 2:
            return False
        
        swap_character = list_s1[diff_list[0]]
        list_s1[diff_list[0]] = list_s1[diff_list[1]]
        list_s1[diff_list[1]] = swap_character
        if "".join(list_s1) != "".join(list_s2):
            return False
        
        return True