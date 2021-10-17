#287. Find the Duplicate Number

#https://leetcode.com/problems/find-the-duplicate-number/submissions/

"""
Given an array of integers nums containing n + 1 integers where each integer 
is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only 
constant extra space.

Input: nums = [1,3,4,2,2]
Output: 2

Input: nums = [3,1,3,4,2]
Output: 3

"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            correct = nums[i]         
            if nums[i] < len(nums) and nums[i] != nums[correct]:
                nums[i] , nums[correct] = nums[correct], nums[i]
            else:
                i+=1
        else:
            i+=1
        return nums[0]