#!/usr/bin/env python
# coding: utf-8

# In[1]:


#There are two loops in python while and for 
#loop is used to execute the set of logic again and again 
#in if condition is checked only once if a>b:, elif b>a:, else
#in while condition is checked until the it becomes false
#while
#genarlly we use counter value in while
counter=1
while counter<=10:
    print("The counter value is:",counter)
    counter=counter+1
#else:
    #print("Value greater than 10 exit")
#else is not compulsary if its there then u can understand that it exited loop with a stmt else is never compulsary
    


# In[13]:


#for loop
#len fun give u the total lenght of list
#range gives u the first and last index of the list
days=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
print(days[0])
print(len(days))
print(range(len(days)))

for i in range(len(days)):
    print ("The day is :",days[i])


# In[14]:


##nested loop
#for loop
days=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
activities=['Yoga','Cardio','Boxing','Dance','Core','strength','gym']
for i in range(len(days)):
    print ("The day is :",days[i])
    for j in range(len(activities)):
        print("The acitivy done is :",activities[j])
        


# In[1]:


days=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
fitness=['Yoga','Boxing','Core','Strengthing','Dance','Cardio','gym']
for i in range(len(days)):
    print("Today is :",days[i])
    for j in range(0,i):
        print("The activity is :",fitness[i])
            


# In[3]:


#specifying range
#python will run from 1 to 6 not 7
#first j=1,1 so it print 1 then j=1,2 it print the same then j=1-3 prints 1,2,3
#two print statements are used to print j and formatting like space and new line
"end= is used to give space at the end of the line

n=5
for i in range(1,n+2):
    for j in range(1,i):
        print(j,end=" ")
    print("\n")


# In[4]:


#we can give range by passing 3rd comma
n=5
for i in range(1,n+2,2):
    print (i)
    for j in range(1,i):
        print(j,end=" ")
    print("\n")


# In[15]:


#loop control statements 
#break, continue, pass
#break-terminates the loop if condition matches 
for i in range(1,11):
    if i==5:
        break
    print(i)
    


# In[16]:


#continue-skips that and just continues the loop if condition matches
for i in range(1,10):
    if i==5:
        continue
    print(i)


# In[17]:


#pass-placeholder suppose when a dev is devoping the code and puts the condition template and inside logic is still unknown use pass- does nothing
for i in range(1,10):
    if i==7:
        pass
    print(i)


# In[20]:


for i in range(1,10):
    if i==6:
        #pass
        print("yeahhhhh its 6......")
    print(i)
        


# In[4]:


#open the file and add the content
newfile=open("EDU_PY2.txt","w+")
for i in range(0,10):
    newfile.write("Hello welcome to python learning\n")
#CHANGING THE CURRENT FILE POSTION AND READ THE FILE 
newfile.seek(1,0)
print(newfile.read())
#READING THE WHOLE TEXT OF A FILE TO A STRING
print("Current file postion",newfile.tell())
newfile.close()
print("Is the file closed ?",newfile.closed)
print("File mode is",newfile.mode)
print("File name is",newfile.name)


# In[ ]:





# In[ ]:





# In[9]:


fname=input("ENTER THE FILENAME:")
word=input("ENTER THE KEYWORD TO BE SEARCHED:")
fname2=input("ENTER THE DESTINATION FILENAME:")
fout=open(fname2,"w")
with open(fname, 'r')as f:
    for line in f:
        words=line,split()
        for i in words:
            if(i ==words):
                fout.write(line)
fout.close()
print("After the kw search")
txt=open(fname2)
print(txt.read())
                


# In[14]:


#Concatenation 
str=2+3
print(str)
Str='Phython '+' '+'is'+' '+'Easy'+''
print(Str)


# In[15]:


#muliplicaion
str='python '*3
print(str)


# In[20]:


#lower
str='python is easy'
str.islower()


# In[27]:


#upper
#str='PHYTHON IS EASy'
#will be false
str='PHYTHON IS EASY'
str.isupper()


# In[47]:


#SLICING[:]
list=['Apples','Mangoes','Bananas','Oranges']
list[2] #using indexing
print("THIS IS USING INDEXING",list[2])
print("using slicing",list[:2])
print("print 1and 2nd index",list[1:2])#since last value we wont get in pyhton
print("using slicing",list[1:3])
print("from 1st index",list[1:])
#we have -1 -2 -3 -4 also along with 0 1 2 3 
print("last value of list",list[-1])
print ("last but 3rd value in a list of 100 strings say",list[-3])
print("last 3 values",list[-3:-1])
print("last 3 values",list[-3:])


# In[55]:


#index===we want the index number of the value then use index
lst=["C","C++","JAVA","UNIX","PERL"]
print("Using format index fun",format(lst.index("UNIX")))
print(lst)
print(lst[1])
print(lst.index("JAVA"))
lst.append("Python")
print(lst)
print(lst[-1])


# In[57]:


#reverse a lst
lst=["red","white","blue","green"]
print("before reversing",lst)
lst.reverse()
print("after revering",lst)


# # USER DEFINED FUNCTIONS

# In[ ]:


#ANLOGY FOR funtions 
#we have a class called python which has some books (fun) availble inside the class wrt python= these are called inbuild functions
#we have a library outside the class called numpy and pandas and others also,if we have to use these func then we have to go and getit/downaload it/import it 
#if we want to write some function other than inbuilt fun like lst.append() instead of lst.thanu() then it is called user defined funtions 


# In[60]:


def greeting(name):
    text=("Hi, Welcome to the python class",name)
    return(text)


# In[61]:


name=input("Enter ur name:")
output=greeting(name)
print(output)
#First run 60 and then run 61


# # Assignment
# #function goodbye
# #that print "have a gud time, ur name "here name is  a input
# def goodbye(name):
#     msg=("Have a good day",name)
#     return(msg)
# name=input("Enter ur name:")
# out=goodbye(name)
# print(out)
# 
# 
# #without return
# def goodbye(name):
#     msg=("Have a nice day",name)
#     print(msg)
#     
# name=input("Enter ur name:")
# goodbye(name)

# In[68]:


#function goodbye #that print "have a gud time, ur name "here name is a input 
def goodbye(name): 
    msg=("Have a good day",name)
    return(msg)
name=input("Enter ur name:")
out=goodbye(name)
print(out)

#without return
def goodbye(name):
    msg=("Have a good day",name)
    print(msg)

name=input("Enter ur name:") 
goodbye(name)
    


# # Here function is called definition ,input is called argument/keyword argument we can also have  a default argument

# In[70]:


def welcome(name="Buddy"):
    msg=("Gud morning",name)
    return(msg)
#default argument

name=input("Hi, Enter ur name")
out=welcome()
print(out)

#Functional argument

name=input("Hi, Enter ur name")
out=welcome(name)
print(out)


# In[6]:


#Two/multiple arguments 

def details(name,age):
    res=("Welcome",name,"Your age is:",age)
    return(res)
out=details("Thanu",30)
print(out)


# #Variable argument- denated by *arg -once if we use this u can pass or cannot pass the arg no restriction
# 
# def details(name,age,*arg):
#     res=("Welcome",name,"Your age is:",age)
#     return(res)
# out=details("Thanushri")
# out=details("Thanushri",30,oct,20)
# print(out)

# In[14]:


#Variable argument- denated by *arg -once if we use this u can pass or cannot pass the arg no restriction

def details(name,age,*arg): 
    res=("Welcome",name,"Your age is:",age) 
    return(res)
out=details("Thanushri",30)
#out=details("Thanushri",30,oct,20)
print(out)


# In[23]:


def purchase(fruits,veggies,*others):
    print("Products purchased are:")
    print(fruits,veggies)
    for item in others:
        print(item)
        
purchase("Mango","ladyfinger")
purchase("Milk","cucmber")
purchase("Grapes","pumpkin","Atta")


# In[26]:


#if we give def value then even when we dont pass the param it consideres the def values this avaids the error 
def stu(name,age=30,*arg):
    print("Student name is",name)
    print("Student age is",age)
stu("Thanu",25)
stu("shri")


# In[32]:


#scope of var
#global
a=30
def num():
    #local
    b=45
    print(b)
print(a)
num()
#will get error print(b)


# In[34]:


a=30
def add(b):
    print("b is ",b)
    c=10+b
    print("Addition is",c)
print(a)
add(15)

    


# In[39]:


#lamba is a function which can be used similar to definition , it is legacy way not used now
#normal way of writting
def fun(z):
    z=z**5
    return(z)
fun(2)

#equvivalent lambda
func=(lambda z:z**4)
print("This is lambda",func(3))


# In[46]:


#this is call by value
#a value actually do not change inside mul_fun,it is just a copy of value 
a=3
print(id(a))
def mul_fun(x):
    x=x**3
    print(x)
    print(id(x))
    return(x)
print(a)
mul_fun(a)


# In[49]:


#call by reference
#list is mutable 
#hence if u pass the value the org value gets change ,hence the id of list remains same

a=["Thanu","Shri"]
print(id(a))
def list_mod(x):
    x.append("BV")
    print(id(x))
    return(x)
print(a)
list_mod(a)


# In[55]:


#inbuilt func
a=[1,22,3,4]
b=sum(a)
print(b)
print(max(a))

#concatenating the string and num 
c="year"+"1234"
print(c)


# In[ ]:




