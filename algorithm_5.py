#coding=utf-8

'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

class Solution(object):
    def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        def is_palidrome(string):
            left = 0
            right = len(string)-1
            while left < right:
                if string[left] == string[right]:
                    left += 1
                    right -=1
                else:
                    return False
            return True
        #print (is_palidrome(s))
        for i in range(len(s)):
            #print('i:',i)
            for j in
            res = s[i:]
            #print('   ',res)
            if is_palidrome(res) == True:
                return res
            res = s[:len(s)-i][::-1]
            #print('   ',res)
            if is_palidrome(res) == True:
                return res
        return None


print (Solution.longestPalindrome('sabcbae'))
