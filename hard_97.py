# -*- coding: utf-8 -*-
# Author: Weichen Liao
'''
97. Interleaving String
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
'''

'''
s1:  aabcc
s2:  dbbca
s3:  aadbbcbcac

a abcc
d bbca
a adbbcbcac 

a a bcc
d bbca
a a dbbcbcac 

aa b cc
d bbca
aa d bbcbcac 

aa b cc
d b bca
aad b bcbcac 

aa b cc
db b ca
aadb b cbcac 

aa b cc
dbb c a
aadbb c bcac 

aa b cc
dbbc a
aadbbc b cac 
'''

#s3的每一个字母，要么从s1里拿一个，要么从s2里拿，难点是当从s1和s2里都可以拿都时候，若之后发现是思路，则需要回到这一步选择另一个。
#这个问题可以用递归来解决
def isInterleave(s1: str, s2: str, s3: str):
    if len(s3) != (len(s1)+len(s2)):
        return False
    if len(s1)==0:
        if s3==s2:
            return True
        else:
            return False
    elif len(s2)==0:
        if s3==s1:
            return True
        else:
            return False
    str1 = s1[0]
    str2 = s2[0]
    str3 = s3[0]
    if str3 == str1 and str3 == str2:
        return isInterleave(s1[1:],s2,s3[1:]) or isInterleave(s1,s2[1:],s3[1:])
    elif str3 == str1:
        return isInterleave(s1[1:],s2,s3[1:])
    elif str3 == str2:
        return isInterleave(s1, s2[1:], s3[1:])
    else:
        return False




s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"


s3 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
"babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
"babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
index=66
s1=s3[:index]
s2=s3[index:]

res = isInterleave(s1,s2,s3)
print(res)
