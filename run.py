# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:53:19 2019

@author: xh
"""

import tkinter
import calculate


# 继承
class Application(object):
    """ 界面，逻辑层分离"""

    def __init__(self):
        '''初始化'''

        self.lists = []  # 设置一个变量 保存运算数字和符号的列表
        self.isPressSign = False  # 添加一个判断是否按下运算符号的标志,假设默认没有按下按钮
        self.isPressNum = False

        self.createWiddgets()  # 初始化界面

    def createWiddgets(self):
        root = tkinter.Tk()  # 实例化
        root.minsize(280, 500)
        root.title('计算器')
        self.result = tkinter.StringVar()
        self.result2 = tkinter.StringVar()

        '''界面'''
        # 界面布局
        # 显示面板
        # self.result.set(0)  # 显示结果1，用于显示默认数字0
        self.result2.set('')

        # 显示板
        label = tkinter.Label(root, font=('楷体', 20), bg='#AFEEEE', bd='9', fg='#F08080', anchor='se',
                              textvariable=self.result2)
        label.place(width=280, height=170)
        label2 = tkinter.Label(root, font=('楷体', 30), bg='#AFEEEE', bd='9', fg='#FF0000', anchor='se',
                               textvariable=self.result)
        label2.place(y=170, width=280, height=60)

        # 数字键盘
        btn7 = tkinter.Button(root, text='7', font=('楷体', 20), fg='#00008B', bd=0.5,
                              command=lambda: self.pressNum('7'))
        btn7.place(x=0, y=285, width=70, height=55)
        btn8 = tkinter.Button(root, text='8', font=('楷体', 20), fg='#00008B', bd=0.5,
                              command=lambda: self.pressNum('8'))
        btn8.place(x=70, y=285, width=70, height=55)
        btn9 = tkinter.Button(root, text='9', font=('楷体', 20), fg='#00008B', bd=0.5,
                              command=lambda: self.pressNum('9'))
        btn9.place(x=140, y=285, width=70, height=55)

        btn4 = tkinter.Button(root, text='4', font=('楷体', 20), fg='#00008B', bd=0.5,
                              command=lambda: self.pressNum('4'))
        btn4.place(x=0, y=340, width=70, height=55)
        btn5 = tkinter.Button(root, text='5', font=('楷体', 20), fg='#00008B', bd=0.5,
                              command=lambda: self.pressNum('5'))
        btn5.place(x=70, y=340, width=70, height=55)
        btn6 = tkinter.Button(root, text='6', font=('楷体', 20), fg='#00008B', bd=0.5,
                              command=lambda: self.pressNum('6'))
        btn6.place(x=140, y=340, width=70, height=55)

        btn1 = tkinter.Button(root, text='1', font=('楷体', 20), fg='#00008B', bd=0.5,
                              command=lambda: self.pressNum('1'))
        btn1.place(x=0, y=395, width=70, height=55)
        btn2 = tkinter.Button(root, text='2', font=('楷体', 20), fg='#00008B', bd=0.5,
                              command=lambda: self.pressNum('2'))
        btn2.place(x=70, y=395, width=70, height=55)
        btn3 = tkinter.Button(root, text='3', font=('楷体', 20), fg='#00008B', bd=0.5,
                              command=lambda: self.pressNum('3'))
        btn3.place(x=140, y=395, width=70, height=55)
        btn0 = tkinter.Button(root, text='0', font=('楷体', 20), fg='#00008B', bd=0.5,
                              command=lambda: self.pressNum('0'))
        btn0.place(x=70, y=450, width=70, height=55)

        # 运算符号按钮
        btnac = tkinter.Button(root, text='AC', bd=0.5, font=('黑体', 20), fg='red',
                               command=lambda: self.pressCompute('AC'))
        btnac.place(x=0, y=230, width=70, height=55)
        btnback = tkinter.Button(root, text='←', font=('楷体', 20), fg='red', bd=0.5,
                                 command=lambda: self.pressCompute('b'))
        btnback.place(x=70, y=230, width=70, height=55)
        btndivi = tkinter.Button(root, text='÷', font=('楷体', 20), fg='#0000FF', bd=0.5,
                                 command=lambda: self.pressCompute('/'))
        btndivi.place(x=140, y=230, width=70, height=55)
        btnmul = tkinter.Button(root, text='×', font=('楷体', 20), fg="#0000FF", bd=0.5,
                                command=lambda: self.pressCompute('*'))
        btnmul.place(x=210, y=230, width=70, height=55)
        btnsub = tkinter.Button(root, text='-', font=('楷体', 20), fg=('#0000FF'), bd=0.5,
                                command=lambda: self.pressCompute('-'))
        btnsub.place(x=210, y=285, width=70, height=55)
        btnadd = tkinter.Button(root, text='+', font=('楷体', 20), fg=('#0000FF'), bd=0.5,
                                command=lambda: self.pressCompute('+'))
        btnadd.place(x=210, y=340, width=70, height=55)
        btnequ = tkinter.Button(root, text='=', bg='orange', font=('楷体', 20), fg=('red'), bd=0.5,
                                command=lambda: self.pressEqual())
        btnequ.place(x=210, y=395, width=70, height=110)
        btnper = tkinter.Button(root, text='%', font=('楷体', 20), fg='#0000FF', bd=0.5,
                                command=lambda: self.pressCompute('%'))
        btnper.place(x=0, y=450, width=35, height=55)

        btnpoint = tkinter.Button(root, text='.', font=('楷体', 20), fg=('#0000FF'), bd=0.5,
                                  command=lambda: self.pressCompute('.'))
        btnpoint.place(x=35, y=450, width=35, height=55)

        leftBrackets = tkinter.Button(root, text='(', font=('楷体', 20), fg=('#0000FF'), bd=0.5,
                                      command=lambda: self.pressCompute('('))
        leftBrackets.place(x=140, y=450, width=35, height=55)

        rightBrackets = tkinter.Button(root, text=')', font=('楷体', 20), fg=('#0000FF'), bd=0.5,
                                       command=lambda: self.pressCompute(')'))

        rightBrackets.place(x=175, y=450, width=35, height=55)
        # 主窗口循环
        root.mainloop()

    # 数字函数
    def pressNum(self, num):  # 设置一个数字函数 判断是否按下数字 并获取数字将数字写在显示版上
        if self.isPressSign == False:
            pass
        else:  # 重新将运算符号状态设置为否
            self.result.set(0)
            self.isPressSign = False

        # 判断界面的数字是否为0
        oldnum = self.result.get()  # 第一步
        if oldnum == '0':  # 如过界面上数字为0 则获取按下的数字
            self.result.set(num)
        else:  # 如果界面上的而数字不是0  则加上新按下的数字
            newnum = oldnum + num
            self.result.set(newnum)  # 将按下的数字写到面板中

    # 运算函数
    def pressCompute(self, sign):
        # try:
        #     if sign == '-':
        #         if self.lists[-1] == '*' or self.lists[-1] == '/'or self.lists[-1] == '(':  #6*9-2   6*-2
        #             self.lists.append('(0')
        # except:
        #     pass

        if sign != '(':
            num = self.result.get()  # 获取界面数字
            self.lists.append(num)  # 保存界面获取的数字到列表中
        #print('1',self.lists)


        # try:
        #     if sign == '-':
        #         if self.lists[-2] == '(0':  #6*9-2   6*-2
        #             self.lists.pop(-1)
        # except:
        #     pass

        #print(self.lists)
        try:
            if self.lists[-2] == ')':
                self.lists.pop(-1)  # 保存界面获取的数字到列表中
        except:
            pass
        self.lists.append(sign)  # 将按下的运算符号保存到列表中
        # print(self.lists
        self.isPressSign = True

        if sign == 'AC':  # 如果按下的是'AC'按键，则清空列表内容，# 讲屏幕上的数字键设置为默认数字0
            self.lists.clear()
            self.result.set(0)
        if sign == 'b':  # 如果按下的是退格‘’，则选取当前数字第一位到倒数第二位
            a = num[0:-1]
            self.lists.clear()
            self.result.set(a)

    # 获取运算结果函数
    def pressEqual(self):
        if self.lists[-1] != ')':
            curnum = self.result.get()  # 设置当前数字变量，并获取添加到列表
            self.lists.append(curnum)

        for i, k in enumerate(self.lists):
            if k == '(0':
                self.lists.insert(i + 3, ')')

        #print(self.lists)
        computrStr = ''.join(self.lists)  # 将列表内容用join命令将字符串链接起来
        print(computrStr)
        cc = calculate.calculating()
        endNum = cc.cal(computrStr)
        self.result.set(endNum)  # 将运算结果显示到屏幕1
        self.result2.set(computrStr)  # 将运算过程显示到屏幕2
        self.lists.clear()  # 清空列表内容


if __name__ == '__main__':
    # 实例化application
    cal = Application()
