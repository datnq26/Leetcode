class Solution(object):
    def mergeArrays(self, nums1, nums2):
        result = {}

        # Process nums1, assuming nums1 is a list of [index, value] pairs
        for index, value in nums1:
            if index in result:
                result[index] += value
            else:
                result[index] = value

        # Process nums2, assuming nums2 is a list of [index, value] pairs
        for index, value in nums2:
            if index in result:
                result[index] += value
            else:
                result[index] = value

        # Convert the dictionary to a list of lists
        res = [[key, value] for key, value in result.items()]
        res.sort(key=lambda x : x[0])
        return res