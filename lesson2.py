# This is a sample Python script. Part I

# none type variables INT
a_int = 5
print(type(a_int)) # echo int
print(id(a_int))  # echo id variable

# none type variables BOOL
a_bool = True
print(a_bool) # echo True

#enable types
#None undefinded
#int, float, complex
#(Sequence Type) list, tuple, range, str
#(Binary Sequence Types) bytes, bytearray, memoryview
#(Set Types) set, frozenset
#(Mapping Types) dict

#some interesting math operations
print(2**2) # echo pow(value,to_value);
print(5//2) # echo division front 2 times
print(5%2) # echo division back 1

#bite operations code on phyton
print(int(0b0101), bin(0b0101), hex(0b0101), end=" ")
print(bin(0b01^0b10), bin(0b01&0b10), bin(0b01|0b10), bin(0b1<<3)) # echo 5 0b101 0x5 0b11 0b0 0b11 0b1000

#modul math
import math
print(math.sqrt(4))

#if else comparsion
if (True):
    print("is true")
elif (False):
    print("is false")
else:
    print("not")

#range function implementation range(from, to, step)
print(list(range(0,10,2)))
print(list(range(10,5,-1)))

#while operator with operators break continue
good = True
go = 0
while(good):
    good  = True if (go<10) else False
    print(go)
    go += 1

#for operators also with
for i in range(1,6,1):
    if (i==5): break
    elif(i==2): continue
    else: print(i, end=" ") #echo 1 3 4

#for strings (one symbol in string is a string with len(1))
str_x = "Hello i am string"
for i in str_x: print(i, end=" ") #echo H e l l o   i   a m   s t r i n g
print(end="\n")

#list simplest exp
b = list()
print(type(b))
b = [1,2,3,4,5.5,6,2,2,'abc']
b.append(666) #insert item or list
b.remove(2)  #remove item key=value
b.extend([14,88]) #extend end of current list by list
a = b.pop(3) #cut from pos and return value
ind = b.index(666) #return index by value
c_int = b.count(2)
print(b, "a", a, "ind", ind, "count(2)", c_int) #echo [1, 3, 4, 6, 2, 2, 'abc', 666, 14, 88] a 5.5 ind 7 count(2) 2
#list.sort(True) sorted up order list.sort(False) sorted down order
#list.reverse()  reversing values order back to front

#list slicing code style [from, to, step]
xl = [1,2,3,4,5,6,7,8,9,10]
print("my_slice", xl[3:9:2], "nosliced", xl) #echo my_slice [4, 6, 8] nosliced [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#tuple looks like constant types array named "cortage"
t = ("abc", [1,2,3], [666,13,"friday"])
for i in range(3): print(t[i][2],end=" ") #echo c 3 friday

#dict as a simple map conteiner(unic! reinserted!)
d = {'b':6,'c':3,'d':4,'a':2,'e':1,'f':0,'f':0,'f':8}
d['h'] = 10 #insert a key-value
del d['a'] #delete key
print (d) #echo {'b': 6, 'c': 3, 'd': 4, 'e': 1, 'f': 8, 'h': 10}
n_d = d.fromkeys([1,2,3], 10) # =dict.fromkeys(seq,value)
print (n_d) #echo {1: 10, 2: 10, 3: 10}
#methods =dict.copy() =dict.get(key) =dict.keys() =dict.items() key,value
#methods =dict.pop(key) return poped key =dict.popitem() return poped item(key,value)

#set order and uniq looks like s = {5,1,6,7,8,9,6,3}
s = {5,1,6,7,8,9,6,3}
print ("set", s) #echo set {1, 3, 5, 6, 7, 8, 9}



#short function exp
def my_func(x,y,z):
    return x*y*z
print(my_func(1,5,6)) #echo 30

#hilty lambda function
double = lambda x,y: x*y
print (double(5,8)) #echo 40

#compare stile lambda expression in some func
l = [1,2,3,4,5,6,7,8,9,10]
nl = list(filter(lambda x : (x%2 == 0), l))
print(nl) #echo [2, 4, 6, 8, 10]

