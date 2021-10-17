# https://leetcode.com/problems/missing-number/submissions/

"""
Given an array nums containing n distinct numbers in the range [0, n], \
return the only number in the range that is missing from the array.

Input: nums = [3,0,1]
Output: 2

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8

"""

#Using cyclic sort algorithm and O(n) time complexity

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        i = 0
        while i < len(nums):
        # for i in range (len(nums)):
            correct = nums[i]         
            if nums[i] < len(nums) and nums[i] != nums[correct]:
                nums[i] , nums[correct] = nums[correct], nums[i]
            else:
                i+=1
        else:
            i+=1
        
        for j in range(len(nums)):
            if nums[j] != j:
                return j
        
        return len(nums)
