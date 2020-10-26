# -*- coding: utf-8 -*-
# Author: Weichen Liao

'''
1513. Number of Substrings With Only 1s
Given a binary string s (a string consisting only of '0' and '1's).

Return the number of substrings with all characters 1's.

Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.
Example 2:

Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.
Example 3:

Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.
Example 4:

Input: s = "000"
Output: 0

1       1
11      3 ((1+1)+1)
111     6 ((1+1+1)+(1+1)+1)
1111    10 ((1+1+1+1)+(1+1+1)+(1+1)+1)
'''

'''
先找出连续的1的子字符串，然后给个子字符串所对应的符合要求的数量是有规律的
'''
def numSub(s: str):
    def getNumForSub(s: str):
        res = 0
        length = len(s)
        while length > 0:
            res += length
            length -= 1
        return res

    res = 0
    subStrList = []
    index = 0
    subStr = ""
    while index < len(s):
        if s[index] == "1":
            subStr += s[index]
        else:
            if subStr != "":
                subStrList.append(subStr)
                subStr = ""
        index += 1
    if subStr != "":
        subStrList.append(subStr)
    print(subStrList)
    for item in subStrList:
        num = getNumForSub(item)
        print(item, num)
        res += num
    return res % 1000000007

s = "1011011101111"
s = ""
s = "101"
s = "111111"
res = numSub(s)
print('res: ',res)