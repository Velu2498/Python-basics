#Sample Code for List :
example = ["hii",2,3.2,"hellow","bii"]
print (example[3])
print (example[4])
example[0]="hay"
print (example[0])



#Sample Code for Tuples :
year_born = ("Paris Hilton", 1981)
print (year_born[0])
print (year_born[1])
#year_born[1] = 2011 __>> any modification will throw error

#Sample Code for Dictionaries :
mydict = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
print ("Cost of apple is " + str(mydict["apples"]))
mydict["apples"] = 800
print ("New Cost of apple is " + str(mydict["apples"]))

confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1] += 1
sum = 0
for k in confusion:
   sum += confusion[k]
print (sum)

names1 = ['Amir', 'Barry', 'Chales', 'Dao']
names2 = names1
names3 = names1[:]
names2[0] = 'Alice'
names3[1] = 'Bob'
sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10
print (sum)



names1 = ['Amir', 'Barry', 'Chales', 'Dao']
loc = names1.index("Chales")
print (loc)

names1 = ['Amir', 'Barry', 'Chales', 'Dao']
names2 = [name.lower() for name in names1]
print (names2[2][0])