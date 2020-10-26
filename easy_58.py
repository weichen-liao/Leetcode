# -*- coding: utf-8 -*-
# Author: Weichen Liao

'''
58. Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5

'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag = False
        lastWord = ''
        for i in range(len(s)):
            if s[i] != " ":
                if flag:
                    lastWord = s[i]
                else:
                    lastWord += s[i]
                flag = False
            else:
                flag = True
        return lastWord

string = "d"

s = Solution()
ans = s.lengthOfLastWord(string)
print(ans)
