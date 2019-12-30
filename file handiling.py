#read the file
file = open("testfile.txt")  
print(file.read()) 

#to rewrite the file
file = open("testfile.txt","w+")  
file.write("Welcome Guvi........") 
file.seek(0)
print(file.read())
#file.close()