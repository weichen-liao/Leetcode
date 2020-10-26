# -*- coding: utf-8 -*-
# Author: Weichen Liao

'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

def longestCommonPrefix(strs):
    res = ""
    index = 0
    while True:
        currStr = ""
        for item in strs:
            try:
                currStr += item[index]
            except:
                return res
        index += 1
        if len(set(currStr)) == 1:
            res += list(set(currStr))[0]
        else:
            break
    return res


strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
strs = ["aa","a"]
res = longestCommonPrefix(strs)
print(res)