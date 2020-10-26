# -*- coding: utf-8 -*-
from scipy.special import comb
'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
# 递归法，但是要考虑性能，很多数会被重复计算，把算过的结果存下来
class Solution:
    def climbStairs(n: int):
        dict_ans = {1:1,2:2}
        def recrusive(n):
            try:
                return dict_ans[n]
            except:
                n_1 = recrusive(n-1)
                dict_ans[n-1] = n_1
                n_2 = recrusive(n-2)
                dict_ans[n-2] = n_2
                return n_1 + n_2
        return recrusive(n)
'''


# 求2元1次方程组的不同解数量: 2x+y=n

class Solution2(object):
    def climbStairs(n):
        def fact(x):  # 做个阶乘函数
            k = 1
            for i in range(1, x + 1):
                k = k * i
            return k

        def c(y, x):  # 做个排列组合函数,y中选x个
            fenzi = fact(y)
            fenmu = fact(x) * fact(y - x)
            return fenzi / fenmu

        a = 0
        for z in range(0, n + 1):
            if (n - z) % 2 == 0:
                t= int((n+z)/2)
                a += c(t, z)
            else:
                continue
        return a
        # ans = 0
        # for i in range(0,n//2+1):
        #     ans = ans + c(n-i,i)  #i是每一个可能的b，组合为 kb = c(n-b,b)，求和kb
        # return ans

'''
class Solution2:
    def climbStairs(n: int):
        def fact(x):  # 做个阶乘函数
            k = 1
            for i in range(0, x + 1):
                k = k * i
            return k

        def c(y, x):  # 做个排列组合函数,y中选x个
            fenzi = fact(y)
            fenmu = fact(x) * fact(y - x)
            return fenzi / fenmu

        a=0
        for y in range(0,n+1):
            if (n-y)%2==0:
        
                a += c((y+(n-y)/2),y)
            else:
                continue
        return a
'''


n = 5
print(Solution2.climbStairs(n))