class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        exists = {}
        for idx, val in enumerate(nums):
            if target - val in exists:
                return [exists[target - val], idx]
            else:
                exists[val] = idx
        return []
