# -*- coding: utf-8 -*-
'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def letterCombinations(digits: str):
        dict_num_to_letter = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        res = []
        first_letter = dict_num_to_letter[int(digits[0])][0]    #a
        # 用来指示第几位数字当前最深遍历到第几个字母了。eg:[2,3,0]中的2表示第一个数字的字母串已经遍历到了第2个字母
        letter_index_indicator = [0 for i in range(len(digits))]
        # 当letter_index_indicator的和等于这个数的时候，算法就结束了
        end_indicator = sum([len(dict_num_to_letter[int(n)]) for n in digits])
        # to check which iteration is now
        iteration_num = 0
        # 深度遍历
        def recrusive(s,index_num,index_letter):
            print('begin of iteration:%i'%iteration_num,' s:%s'%s, 'index_num:%i'%index_num, 'index_letter:%i'%index_letter)
            if len(s) == len(digits):
                res.append(s)
                return s

            if index_num < len(digits)-1:
                this_letter = dict_num_to_letter[int(digits[index_num])][letter_index_indicator[index_num]]
                s = recrusive(s + this_letter, index_num+1, letter_index_indicator[index_num+1])
                s = s[:-1]
            if letter_index_indicator[index_num] < len(dict_num_to_letter[int(digits[index_num])]):
                this_letter = dict_num_to_letter[int(digits[index_num])][letter_index_indicator[index_num]+1]
                s = recrusive(s + this_letter, index_num, index_letter)
                s = s[:-1]
                if
        # def recrusive(s,index_num,index_letter,iteration_num):
        #     print('begin of iteration:%i'%iteration_num,' s:%s'%s, 'index_num:%i'%index_num, 'index_letter:%i'%index_letter)
        #     if len(s) == len(digits):
        #         res.append(s)
        #         return s
        #     this_num = digits[index_num]    #2      3
        #     this_letters = dict_num_to_letter[int(this_num)]    #abc        def
        #     #while sum(letter_index_indicator) < end_indicator:
        #     if index_num < len(digits)-1:
        #         index_num += 1  #1
        #         next_num = digits[index_num]    #3
        #         next_letters = dict_num_to_letter[int(next_num)]    #def
        #         iteration_num += 1  #1
        #         s = recrusive(s + next_letters[0],index_num,0,iteration_num=iteration_num)
        #         print('  this one finished')
        #         s = s[:-1]
        #         #index_num -= 1
        #         this_num = digits[index_num]
        #         this_letters = dict_num_to_letter[int(this_num)]
        #
        #         while index_letter < len(this_letters)-1:
        #             index_letter += 1
        #             iteration_num += 1
        #             s = recrusive(s + this_letters[index_letter],index_num,index_letter, iteration_num=iteration_num)
        #             s = s[:-1]
        #         print ('  ok, the index_letters run out')
        #
        #     index_num -= 1
        #     index_letter = 0
        #     print('end of iteration:%i' % iteration_num, ' s:%s' % s, 'index_num:%i' % index_num,'index_letter:%i' % index_letter)
        #     return s



        recrusive(first_letter, 0, 0, 0)
        print(res)

digits='23'
Solution.letterCombinations(digits)








