'''list=[10,20,30,40,50,60]
increased_marks=[]
for x in list:
    increased_marks.apppend(x+20)
print (increased_marks)'''


#Inline Comprehension:
list=[10,20,30,40,50,60]
print ([x+30 for x in list])

#Comprehension using function:
def fun(x):
    return x+30
increased_marks1 = [fun(x) for x in list]
print(increased_marks1)

#More List Comprehension:
S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]
print (S)
print (V)
print (M)

vec = [2, 4, 6]
print ([3*x for x in vec if x > 3])



vec = [2, 4, 6]
x1 = [ x**2 for x in vec]
print (x1)

