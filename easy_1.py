# -*- coding: utf-8 -*-
# Author: Weichen Liao

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

def twoSum(nums, target):
    indexSorted = sorted(range(len(nums)), key=lambda k: nums[k])
    print(nums)
    print(indexSorted)
    left = 0
    right = len(nums)-1
    while left < right:
        if nums[indexSorted[left]] + nums[indexSorted[right]] == target:
            return sorted([indexSorted[left], indexSorted[right]])
        elif nums[indexSorted[left]] + nums[indexSorted[right]] < target:
            left += 1
        else:
            right -= 1


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    nums = [11, 7, 15, 2]
    nums = [3,3]
    target = 6
    print(twoSum(nums,target))
