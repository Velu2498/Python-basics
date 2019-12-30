Jarvis =['velu','vimal','karthi','arul','sharan','siva','valla']
for i in range(7):
     b = Jarvis[i].upper()
     print(b)
#01
Jarvis =['velu','vimal','karthi','arul','sharan','siva','valla']
def upper():
 for i in range(7):
     b = Jarvis[i].upper()
    
print ([upper() for x in Jarvis ])
#02
def f(string, n, c=0):
    if c < n:
        print(string * n)
        f(string, n, c=c + 1)

f('guvi', 5)
hello = open("one.txt","a")
print ("name of file is", hello.name)

vec = [2, 4, 6]
x1 = [ x**2 for x in vec]
print (x1)