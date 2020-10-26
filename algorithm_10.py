# -*- coding: utf-8 -*-
'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def isMatch(s: str, p: str) -> bool:
        print('s:',s)
        print('p:',p)
        index_s, index_p = 0, 0
        s_p = ''
        flag_s = False
        while index_s <= len(s)-1 and index_p <= len(p)-1:
            # case 1
            if p[index_p] == '*':
                if s_p == '' or s_p == '.':
                    s_p = s[index_s]
                    index_s += 1
                else:
                    if s[index_s] != s_p:
                        if not flag_s:
                            print('case 1  ','s_p:',s_p,'  p[index_p]:',p[index_p],'  index_p:',index_p,'  s[index_s]:',s[index_s],'  index_s:',index_s)
                            return False
                            #index_s += 1
                            #index_p += 1
                        else:
                            index_p += 1
                            s_p = s[index_s]
                            continue
                    else:
                        index_s += 1
                        flag_s = True
            # case 2
            elif p[index_p] == '.':
                if s_p == '':
                    index_s += 1
                    index_p += 1
                else:
                    if s[index_s] != s_p:
                        print('case 2  ', 's_p:', s_p, '  p[index_p]:', p[index_p], '  index_p:', index_p,'  s[index_s]:', s[index_s], '  index_s:', index_s)
                        return False
                    else:
                        s_p = p[index_p]
                        index_s += 1
                        index_p += 1
            # case 3
            else:
                s_p = p[index_p]
                if s[index_s] != s_p:
                    if index_p <= len(p)-1:
                        if p[index_p + 1] == '*':
                            index_s += 1
                            index_p += 1
                            continue
                        else:
                            print('case 3  ', 's_p:', s_p, '  p[index_p]:', p[index_p], '  index_p:', index_p, '  s[index_s]:',s[index_s], '  index_s:', index_s)
                            return False
                    else:
                        print('case 3  ', 's_p:', s_p, '  p[index_p]:', p[index_p], '  index_p:', index_p,
                              '  s[index_s]:', s[index_s], '  index_s:', index_s)
                        return False

                else:
                    index_s += 1
                    index_p += 1
        if index_p < len(p)-1 or index_s <= len(s)-1:
            print('final stage',' s_p:', s_p, '  index_p:', index_p,'  index_s:', index_s)
            return False
        print('return true  ', ' s_p:', s_p, '  index_p:', index_p,'  index_s:', index_s)
        return True

class Solution2:
    def isMatch(s: str, p: str) -> bool:
        index_p, index_s = 0,0
        this_p = p[index_p]
        this_s = s[index_s]
        while index_p <= len(p)-1 and index_s <= len(s)-1:

            if index_p < len(p)-1:
                next_p = p[index_p + 1]
            else:
                next_p = ''
            print('this_p:%s' % this_p,' next_p:%s'%next_p)
            if this_p == '.':
                if next_p != '*':
                    index_s += 1
                    index_p += 1
                else:
                    while index_s<len(s)-1 and s[index_s]==this_s:
                        index_s += 1
                    this_s = s[index_s]
                    index_p += 2
            # this_p not in ['.','*']
            else:

                if next_p != '*':
                    if this_s == this_p:
                        index_s += 1
                        index_p += 1
                    else:
                        return False
                else:
                    while index_s<len(s)-1 and s[index_s]==this_s:
                        index_s += 1
                    this_s = s[index_s]
                    index_p += 2
        print('index_p:%s'%str(index_p),'index_s:%s'%str(index_s))
        if index_p < len(p)-1 or index_s < len(s)-1:
            return False
        return True



s = 'aaa'
#s = 'ab'
#s = "aab"
#s = "mississippi"
#s = ''
#p = "mis*is*p*."
#p = "c*a*b"
#p = 'a'
p = 'a*b'
#p = '.*'
print(Solution2.isMatch(s,p))


