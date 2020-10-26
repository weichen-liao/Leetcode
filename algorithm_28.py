# -*- coding: utf-8 -*-
'''
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hellao", needle = "lla"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Solution:
    def strStr(haystack: str, needle: str) -> int:
        index = 0
        if len(haystack) < len(needle):
            return -1
        if haystack == '' or needle == '':
            return 0
        while index <= len(haystack)-len(needle):
            flag = False
            print(haystack[index])
            for i in range(len(needle)):
                print('  ',haystack[index+i],needle[i])
                if haystack[index+i] != needle[i]:
                    flag = True
                    break
            if flag == False:
                return index
            index += 1
        return -1


class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        if len(haystack) < len(needle):
            return -1
        if haystack == '' or needle == '':
            return 0
        while index <= len(haystack)-len(needle):
            if haystack[index:index+len(needle)] == needle:
                return index
            else:
                index += 1
        return -1


haystack = 'abab'
needle = 'ba'
res = Solution.strStr(haystack,needle)
print(res)

