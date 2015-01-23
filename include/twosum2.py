class Solution:
    # input numbers are sorted in ascending order
    # @return a tuple, (index1, index2)
    def twoSum(self, numbers, target):
        index1 = 0
        index2 = len(numbers) - 1
        while index1 < index2:
            idx_sum = numbers[index1] + numbers[index2]
            if idx_sum > target:
                index2 -= 1
            elif idx_sum < target:
                index1 += 1
            else:
                return (index1 + 1, index2 + 1)
