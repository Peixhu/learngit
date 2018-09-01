class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        :hash table
        """
        if len(nums) <= 1:
            return
        hash_table = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_table :
                return (hash_table[complement],i)
            hash_table[nums[i]] = i
            