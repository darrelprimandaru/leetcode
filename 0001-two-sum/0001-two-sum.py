class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rlist = []

        for a, b in enumerate(nums):
            for c, d in enumerate(nums):
                if a == c:
                    break
                else:
                    test = b + d
                
                if test == target:
                    rlist.append(c)
                    rlist.append(a)
                    return rlist