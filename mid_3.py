# -*- coding: utf-8 -*-
# Author: Weichen Liao

'''
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    # 窗口滑动浪费了时间，左索引移动到下一个字符的时候，右索引不用回去
    def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        flag_break = False
        while len(s)>=1 and flag_break!=True:
            substr = ''
            for i,item in enumerate(s):
                substr += item
                print(substr)
                if len(substr) == len(set(substr)):
                    if i != len(s)-1:
                        continue
                    else:
                        res = max(res, len(substr))
                        flag_break = True
                else:
                    res = max(res,len(substr)-1)
                    s = s[1:]
                    break
        return res


class Solution2(object):
    # 窗口滑动浪费了时间，左索引移动到下一个字符的时候，右索引不用回去
    def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        left = 0
        right = 1
        while right <= len(s):
            string = s[left:right]
            print(string)
            if len(string) == len(set(string)):
                right += 1
                res = max(res, len(string))
            else:
                res = max(res,len(string)-1)
                left += 1
        return res


#s ='abcabcbb'
#s = 'bbbbb'
#s = 'pwwkew'
s = 'a'
#s = 'abcdaebcd'
print (Solution2.lengthOfLongestSubstring(s))




