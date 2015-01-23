class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, numbers, target):
        mappings = {}
        idx_pair = ()
        num_len = len(numbers)
        for i in xrange(0, num_len):
            oppo = target - numbers[i]
            if oppo in mappings:
                idx_pair = (mappings[oppo] + 1, i + 1)
                break
            else:
                mappings[numbers[i]] = i
        return idx_pair
        