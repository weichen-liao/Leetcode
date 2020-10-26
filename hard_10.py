# -*- coding: utf-8 -*-
# Author: Weichen Liao

'''

10. Regular Expression Matching

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

'''

class Solution:
    def isMatch(s: str, p: str) -> bool:
        ans = False
        indexS, indexP = 0, 0
        curP = ''

        # understand the patterns
        patternList = []
        while indexP < len(p):
            if p[indexP] == '*':
                curP += p[indexP]
                patternList.append(curP)
                curP = ''

            else:
                if curP != '':
                    patternList.append(curP)
                curP = p[indexP]

            indexP += 1
        if curP != '':
            patternList.append(curP)
        print('patternList:', patternList)

        # compare with the patterns
        indexP = 0
        flagStar = False
        strStar = ''
        while indexS < len(s) and indexP < len(p):
            curP = patternList[indexP]
            if flagStar == True:
                if curP == '.*':
                    if s[indexS] == strStar:
                        indexS += 1
                        continue
                    else:
                        flagStar = False
                        indexS += 1
                        indexP += 1
                        continue
                else:   #curP == 'm*' like that
                    if s[indexS] == strStar:
                        indexS += 1
                        continue
                    else:
                        flagStar = False
                        indexS += 1
                        indexP += 1
                        continue
            else:
                if curP == '.':
                    indexP += 1
                    indexS += 1
                elif curP == '.*':
                    flagStar = True
                    strStar = s[indexS]
                    indexS += 1
                    continue
                elif '*' in curP:
                    flagStar = True
                    strStar = s[indexS]
                    indexS += 1
                    continue
                # the normal characters
                else:
                    if p[indexP] == s[indexS]:
                        indexP += 1
                        indexS += 1
                    else:
                        return False
        if indexS < len(s) or indexP < len(p):
            return False
        return True
                


s = "misf"
p = "mis.*"
res = Solution.isMatch(s,p)
print(res)
