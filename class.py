class MyClass:
    "This is my second class"
    a = 10
    def func(self):
        print('Hello')
ob = MyClass()
print(MyClass.func)
print(ob.func)
ob.func()

list1 = [2,4,6,8,10,12,14,16,18,20]
print (list1[0:1],list1[5:7]) 

print('%.2f' % 123.444) 