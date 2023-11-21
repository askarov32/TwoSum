class Solution(object):
     def twoSum(self, nums, target):
        dict = {}
        for i,n in enumerate(nums):
            if n in dict:
                return dict[n],i
            else:
                dict[target-n]=i 
