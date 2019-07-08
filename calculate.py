# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 22:58:30 2019

@author: xh
"""

import re


class calculating():
    def cal(self, expre):
        expre = self.replaceOperator(expre)
        list = self.splitStr(expre)
        results = self.deBrackets(list)
        return results

    # 格式化
    def replaceOperator(self, expre):
        expre = expre.replace(" ", "")
        expre = expre.replace("+-", "-")
        expre = expre.replace("--", "+")
        expre = expre.replace("-+", "-")
        return expre

    def splitStr(self, expre):
        # 将整个字符串切割
        str = re.split(r"(\D)", expre)  # 指定分割符用（）括起来，表示保留匹配项
        # print(str)
        # str.pop()
        print(str)
        for index, i in enumerate(str):  # 剔除‘’
            if i == '':
                str.pop(index)
        # print(str)
        return str

    # + - * / 的计算

    def computer(self, list):
        #    list = []
        # 先乘除，在加减
        while '.' in list or '*' in list or '/' in list or '%' in list:
            for index, i in enumerate(list):
                if i == '.':
                    result =float(list[index + 1]) * pow(0.1, len(str(list[index + 1]))) + float(list[index - 1])
                    list[index - 1] = result
                    for j in range(2):
                        list.pop(index)
                elif i == '*':
                    result = float(list[index - 1]) * float(list[index + 1])
                    list[index - 1] = result
                    for j in range(2):
                        list.pop(index)
                elif i == '/':
                    if float(list[index + 1]) == 0:
                        return "error"
                    result = float(list[index - 1]) / float(list[index + 1])
                    list[index - 1] = result
                    for j in range(2):
                        list.pop(index)
                elif i == '%':
                    result = float(list[index - 1]) % float(list[index + 1])
                    list[index - 1] = result
                    for j in range(2):
                        list.pop(index)
        while '+' in list or '-' in list:
            for index, i in enumerate(list):
                if i == '+':
                    result = float(list[index - 1]) + float(list[index + 1])
                    list[index - 1] = result
                    for j in range(2):
                        list.pop(index)
                elif i == '-':
                    result = float(list[index - 1]) - float(list[index + 1])
                    list[index - 1] = result
                    for j in range(2):
                        list.pop(index)
        return list[0]

    def deBrackets(self, str_list):
        #    str_list = []
        #    print(str_list)
        while "(" in str_list:
            count = 0
            # 找到第一个反括号），向前找第一个（
            for index, i in enumerate(str_list):
                if i == ')':
                    count = index
                    # print(count)
                    for m in range(count, -1, -1):
                        if str_list[m] == '(':
                            # 将两个括号里面的元素赋值给一个新的列表，传入计算函数
                            list = str_list[m + 1:count]
                            print(list)
                            # 计算函数（list）返回值赋值给新的数插入到原列表
                            new_str = self.computer(list)
                            # 删除count,和m之间的元素
                            str_list.insert(m, str(new_str))
                            for j in range(count - m + 1):
                                str_list.pop(m + 1)
                            break
        compute = self.computer(str_list)
        if compute != 'error':
            compute = round(compute, 2)
        return compute
