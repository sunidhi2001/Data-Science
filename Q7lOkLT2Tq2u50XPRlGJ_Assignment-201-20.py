
# coding: utf-8

# # Assignment 1

# ## OUTPUT VARIABLES
# 

# In[ ]:


x= 5      #(which is a numeric data-type) 
y="John"  #(which is a string data-type) 
z=True    #(which is a boolean data-type) 
print (x) 
print (y) 
print (z)


# In[3]:


x = 10


# In[4]:


print(x)


# In[5]:


x = 5
print(x)


# In[6]:


X = 7 
print(X) 
print(x)


# ## DATA TYPES IN PYTHON

# In[7]:


print(type(x)) 
print(type(y)) 
print(type(z))


# In[8]:


type(x)
type(y)
type(z)


# ## OPERATORS IN PYTHON
# 

# ARITHMETIC OPERATORS
# 

# In[9]:


2+3


# In[10]:


3-5


# In[11]:


3*8


# In[12]:


24/2


# In[13]:


2**6


# In[14]:


5//4


# In[15]:


6//4


# In[16]:


8//4


# In[17]:


6%4


# In[18]:


7%4


# In[19]:


# These operations are executed in reverse order of appearance. 
2+3*5**2


# In[20]:


# Now the addition comes first and the exponentiation comes last.
((2+3) * 5 )**2


# ASSIGNMENT OPERATORS

# In[21]:


a = 21 
a += 9 
print ("Line 1 - Value of a is ", a) 
a-=9 
print ("Line 2 - Value of a is ", a) 
a*=9 
print ("Line 3 - Value of a is ", a) 
a/=9 
print ("Line 4 - Value of a is ", a) 
a%=9 
print ("Line 5 - Value of a is ", a) 
a**=9 
print ("Line 6 - Value of a is ", a) 
print("Check", 3*3*3*3*3*3*3*3*3) 
a//=9 
print ("Line 7 - Value of a is ", a) 
print ("Check:", 19683//9)


# In[22]:


#a=9 
a+=9 
print(a)


# COMPARISON OPERATORS
# 

# In[23]:


x=9 
y=13 
x==y 
print("Is x == y?", x==y) 
x!=y 
print("Is x!=y?", x!=y) 
x>y 
print("Is x>y?", x>y) 
x<y 
print("Is x<y?", x<y) 
x>=y 
print("Is x>=y?", x>=y) 
x<=y 
print("Is x<=y?", x<=y)


# LOGICAL OPERATORS
# 

# In[24]:


x=110 
y=200 
z=300 
x>150 or y>150


# In[25]:


x>=100 and y>150


# In[26]:


x>=100 and y>150


# In[27]:


not (x>=100 and y>150)   #REVERSING THE RESULT BY USING NOT


# IDENTITY OPERATORS
# 

# In[29]:


x=100 
y=100


# In[30]:


x is y


# In[31]:


x=300 
y=300


# In[32]:


x is y


# In[33]:


x=-4 
y=-4


# In[34]:


x is y


# ## MEMORY STRUCTURE IN PYTHON
# 

# In[35]:


a=10 
b=10 
c=10 
id(a), id(b), id(c)


# In[37]:


a+=1 
id(a)


# In[39]:


x=500 
y=500
print(id(x) , id(y))
x is y


# In[40]:


s1='hello' 
s2='hello' 
id(s1), id(s2)


# In[41]:


s1==s2


# In[42]:


s1 is s2


# In[43]:


s3='hello world!' 
s4='hello world!' 
s3==s4


# In[44]:


s3 is s4


# ## STRING FUNCTIONS
# 

# Strip()

# In[45]:


A = "  Python is a language" 
print(A.strip()) 
print(A)


# Len()

# In[46]:


A = "Python is a language" 
print(len(A))


# In[49]:


x = "This is a class" 
print(len(x))


# In[51]:


len(A)


# In[52]:


A.upper()


# In[53]:


A


# Count()
# 

# In[54]:


A = "Python is a language" 
print(A.count("g"))


# LOWER()
# 

# In[55]:


A = "Python is a language" 
print(A.lower())


# UPPER()
# 

# In[56]:


A = "Python is a language" 
print(A.upper())


# In[57]:


A=input("Enter your name ")


# In[58]:


print(type(A))


# In[59]:


A = input("Enter Number")


# In[60]:


type(A)


# In[61]:


x = float(input("Enter Number"))


# In[62]:


print(x) 
print(type(x))


# TITLE()
# 

# In[63]:


A = "Python is a language" 
print(A.title())


# FIND()
# 

# In[65]:


A[0]


# In[66]:


A[5]


# In[67]:


A[0:4]     #[start_index, stop_index] inclusive, exclusive


# In[68]:


A[10]


# In[69]:


A.find("z")
# If the substring does not appear, find() returns -1:


# In[70]:


A.find("L")


# REPLACE()
# 

# In[72]:


A = "Python is a language" 
print(A.replace("a", "z"))


# SPLIT()
# 

# In[73]:


##  Splitting each word into a separate element in a list: 
A = "Python is a language" 
print(A.split())


# In[74]:


## Splitting by any other character in the string: 
A = "Python is a language"
print(A.split("a"))


# ## CONCATENATE

# In[75]:


"Python" + " is a language"


# In[76]:


String = "Hello People" 
print(String + " This is a lovely morning")


# Str.format()
# 

# In[77]:


name = "Jack" 
age = 10 
city = "Paris" 
String1 = "My name is {} I am {} and I live in {}" 
String1.format(name, age, city)


# STRING INPUT
# 

# In[78]:


x=input("Enter your name:") 
print("Welcome,", x)

