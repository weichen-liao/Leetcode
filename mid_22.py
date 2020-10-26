# -*- coding: utf-8 -*-
import time
'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def generateParenthesis(n: int):
        if n == 0:
            return []
        res = []
        def recursive(s,num_left,num_right):
            #print('iteration begin,s:%s'%s,' num_left:%i'%num_left,' num_right:%i'%num_right)
            #time.sleep(2)
            #while num_left>0 or num_right>0:
            if len(s) == 2*n:
                res.append(s)
                #print(' return s:', s)
                return s
            if num_left>0:
                #print('  go left')
                num_left -= 1
                # 每加一个左括号，就给当前可加的右括号数+1
                num_right += 1
                s = recursive(s+'(',num_left,num_right)
                #print('    after left recursive,s:',s)
                s = s[:-1]
                # 回溯完成后，要给左右可添加的库存恢复回去
                num_left += 1
                num_right -= 1

            if num_right>0:
                #print('  go right')
                num_right -= 1
                # 每加一个右括号，就给当前可加的右括号数-1
                s = recursive(s+')',num_left,num_right)
                #print('    after right recursive,s:', s)
                #print('    s:',s)
                s = s[:-1]
                num_right += 1
            #s = s[:-1]
            #print(' return s:',s)
            return s

        recursive('(',n-1,1)
        return res

print (Solution.generateParenthesis(3))