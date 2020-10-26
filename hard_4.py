# -*- coding: utf-8 -*-
# Author: Weichen Liao
'''
4. Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''


class Solution:
    # 先两个list排序合并，再取median
    def findMedianSortedArrays(nums1, nums2):
        index1 = 0
        index2 = 0
        res = []
        while (index1<len(nums1) and index2<len(nums2)):
            if nums1[index1] < nums2[index2]:
                res.append(nums1[index1])
                index1 += 1
            else:
                res.append(nums2[index2])
                index2 += 1
        res.extend(nums1[index1:])
        res.extend(nums2[index2:])
        if len(res) % 2 == 1:
            return res[int(len(res)/2)]
        else:
            return (res[int(len(res)/2)] + res[int(len(res)/2-1)])/2



nums1 = [1, 3]
nums2 = [4, 6]
res = Solution.findMedianSortedArrays(nums1, nums2)
print(res)

