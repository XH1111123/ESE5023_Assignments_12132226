# 1. Flowchart:
#[10 points] Write a function Print_values with arguments a, b, and c to reflect the following flowchart. Here the purple parallelogram operator is to print values in the given order. Report your output with some random a, b, and c values.

print("T1")

import random

def Print_values():
   a = float(input("Input a = "))
   b = float(input("Input b = "))
   c = float(input("Input c = "))

   if a>b:
       if b>c:
           print(str(a)+", "+str(b)+", "+str(c))
       else:
           if a>c:
               print(str(a)+", "+str(c)+", "+str(b))
           else:
               print(str(c)+", "+str(a)+", "+str(b))
   else:
       if b>c:
           print(str(c)+", "+str(a)+", "+str(b))
       else:
           print(str(c)+", "+str(b)+", "+str(a))

Print_values()

print ("---------------------")

# 2.Matrix multiplication
#2.1 [5 points] Make two matrices M1 (5 rows and 10 columns ) and M2 (10 rows and 5 columns ); both are filled with random integers from 0 and 50.
#2.2 [10 points] Write a function Matrix_multip to do matrix multiplication, i.e., M1 * M2. Here you are ONLY allowed to use for loop, * operator, and + operator.

print("T2")

import numpy as np
M1 = np.random.randint(0,50, size=(5, 10))
M2 = np.random.randint(0,50, size=(10, 5))

print("M1:")
print(M1)
print("M2:")
print(M2)

def Matrix_multip():
    a=np.zeros((5,5)) #5*5 0 matrix
    for i in range(0,5):
        for j in range(0,5):
            for m in range(0, 10):
                for n in range(0, 10):
                    a[i][j]=M1[i][m]*M2[n][j]
    print("M1*M2:")
    print(a)
    return a
Matrix_multip()

print ("---------------------")

#3. Pascal triangle
#[20 points]One of the most interesting number patterns is Pascal’s triangle (named after Blaise Pascal). Write a function Pascal_triangle with an argument k to print the kth line of the Pascal triangle. Report Pascal_triangle(100) and Pascal_triangle(200).

print("T3")

import numpy as np
def Pascal_triangle(k):
    K = np.zeros((k, k))
    for x in range (0,k):
        K[x][0]=1
        K[x][x]=1
        for i in range(2,k):
            for j in range(1,i):
                K[i][j]=K[i-1][j-1]+K[i-1][j]
    #test print(K)
    print("The "+str(k)+"th line of the Pascal_triangle is:")
    print(K[k-1])
    #for i in range(1,k+1):
     #   if i%2==0:

Pascal_triangle(100)
Pascal_triangle(200)
print ("---------------------")


# 4. Add or double
# [20 points] If you start with 1 RMB and, with each move, you can either double your money or add another 1 RMB, what is the smallest number of moves you have to make to get to exactly x RMB? Here x is an integer randomly selected from 1 to 100. Write a function Least_moves to print your results. For example, Least_moves(2) should print 1, and Least_moves(5) should print 3.

print("T4")

def Least_moves():
    x=random.randint(1,100)
    # test x=2 and x=5
    print ("When x="+str(x))
    for i in range(1,x):
        if pow(2,i-1)<x<pow(2,i):
            if x-pow(2,i-1)>pow(2,i):
                b=i+(pow(2,i)-x)
                break
            else:
                b=(i-1)+(x-pow(2,i-1))
                break
    # test print(i)
    print("The smallest number of moves is "+str(b))

Least_moves()
print ("---------------------")


# 5. Dynamic programming
# Insert + or - operation anywhere between the digits 123456789 in a way that the expression evaluates to an integer number. You may join digits together to form a bigger number. However, the digits must stay in the original order.
# 5.1 [30 points] Write a function Find_expression, which should be able to print every possible solution that makes the expression evaluate to a random integer from 1 to 100. For example, Find_expression(50) should print lines include: 1−2+34+5+6+7+8−9=50 and 1+2+34−56+78−9=50
# 5.2 [5 points] Count the total number of suitable solutions for any integer i from 1 to 100, assign the count to a list called Total_solutions. Plot the list Total_solutions, so which number(s) yields the maximum and minimum of Total_solutions?

print ("T5")

import random
import numpy as np
from collections import Counter

def sjz(r):
    yushu = []
    R=int(r)
    while R != 0:
        s=R%3
        yushu.append(s)
        R=R//3
    yushu.reverse()
    T = ''.join(str(s) for s in yushu)
    t = T.zfill(9)   #3^9（三进制1000000000）
    # print(t)  #test
    return t

# Xingyu Nan and Tianci Jiang explained to me how to use ternary in T5.1
# 十进制转三进制方法参考：https://blog.51cto.com/u_16213459/7819614

def Find_expression(x):

    K1 = []
    for u in range(0, pow(3, 9)):
        K1.append(sjz(u))
    # print(K1)  # test
    K2 = []

    for j in range(0,pow(3, 9)):
        A = ""  # 储存式子
        sum = 0  # 除了最后一项的和
        b = 0  # 待加的最后一项
        c = 0  # 运算符号
        for i in range(1,10):
            M1="1"+K1[j]        #读取1个str，前面加1，变成int时保留前面的0
            M2=int(M1)
            a = (M2 // pow(10, 9 - i))%10     #依次取出符号
            #print("M1 : " + str(M1)) #test
            #print("M2 : " + str(M2)) #test
            #print("a : " + str(a)) #test
            #a=random.randint(0,2) #test
            if a==1:  #+
                A=A+"+"+str(i)
                sum=sum+b
                b=i
                c=a
            elif a==2: #-
                A=A+"-"+str(i)
                sum=sum+b
                b=-i
                c=a
            else:
                A = A+str(i)
                if i==1:
                    c=1
                    break  #首个是+1、1重复，去掉1开头的
                if c==1:
                    b = b*10+i
                elif c==2:
                    b = b*10-i
        if i==9:  # test
          sum = sum + b
          K2.append(sum)
          if x==sum:
              print(str(x)+"="+A)

    Total_solutions = []  #T5.2

    for d in range(1,101):
        Total_solutions.append(K2.count(d)) #结果为i的个数

    suoying_max=[]    #检查有没有多个最大值、最小值
    suoying_min = []
    for e1 in range(0,100):
        if Total_solutions[e1]==max(Total_solutions):
            suoying_max.append(e1+1)
        if Total_solutions[e1]==min(Total_solutions):
            suoying_min.append(e1+1)

    #print("Total_solutions: " + str(Total_solutions))   #test
    print("The maximum number(s): " + str(suoying_max))
    print("The minimum number(s) : " + str(suoying_min))

  #  print("i : "+str(i))   #test
  #  print("A : "+str(A))   #test
  #  print("sum : "+str(sum))   #test
  #  print("b : "+str(b))   #test
  #  print("c : " + str(c))   #test

Find_expression(50)










