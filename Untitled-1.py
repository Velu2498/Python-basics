for letter in 'Python':
   print ('Current Letter :' + letter)
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:    
   print ('Current fruit :', fruit)
sum=0
for i in range(5):
    sum=sum+i
    print (sum)
print ("Good bye!")

count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1
print ("Good bye!")

x = sum(range(3))
print(x)

x = 12
y = 18
x = y
y = x
print(x,y)  

x = 1
y = "2"
z = 3
sum = 0
for i in (x,y,z):
    if isinstance(i, int):
        sum += i
print (sum)

x=0 
for i in range(2, 10, 2):
    x = x + i
    print(x) 

x = 1
print(++++x)

colors = ['Red', 'Black', 'White', 'Green']
if "green" in colors:
   print("Green Color")
else:
   print("No Green Color")

s = "Hello there"
a = s.islower()
b = s.lower() 
print(a)
print(b)

def f(n):
    return n*n
a = f(2)
print(a)


num1 = 5
if num1 >= 91:
    num2 = 3
else:
    if num1 < 6:
        num2 = 4
    else:
        num2 = 2
x = num2 * num1 + 1
print (x,x%7)

a=int(input("Please Enter a Number : "))
if(a%2==0):  
    print("This Number is Even")  
else:  
    print("This Number is Odd")  

i=0
while i<5:
 print("Hellow")
 i+=1