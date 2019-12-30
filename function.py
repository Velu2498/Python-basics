listc = ["hii",2,3.2,"hellow","bii"]
def foo(x):
    print( x*3)
def my (fun):
    for item in listc:
        fun(item)

my (foo)


def method1(self):
        return 'howdy python'
def method2(self, methodToRun):
        result = methodToRun()
        return result
def method3(self):
        return self.method2(self.method1)


'''test = Test()
print (test.method3())'''

