# -*- coding: utf-8 -*-
import numpy as np
'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution1:
    def convert(s: str, numRows: int) -> str:
        rows = ['' for i in range(numRows)]
        i, count = 0,0
        positive_direction = True
        while count <= len(s)-1:
            rows[i] += s[count]
            count += 1
            if i >= len(rows) - 1:
                i -= 1
                positive_direction = False
            elif i <= 0:
                i += 1
                positive_direction = True
            else:
                if positive_direction:
                    i += 1
                else:
                    i -= 1
        res = ''.join(rows)
        return res


class Solution2:
    def convert(s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)


s = "LEETCODEISHIRING"
numRows = 4
print(Solution1.convert(s,numRows))







