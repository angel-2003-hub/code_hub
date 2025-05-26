import numpy as np
#Task 1

#program 1

num1=[1,2,3,4,5,6,7,8]
num2=np.array([num1])
print("Numpy Array:",num2)
print("Data Type of numbers:",num2.dtype)

#program 2

num1=[1,2,3,4,5,6,7,8,9]
matrix=[[1,2,3],[4,5,6],[7,8,9]]
num1_array=np.array([matrix])
print(num1_array)

#Task 2
#operators

#ARANGE

numbers=np.arange(11)
numbers_arr=np.array(numbers)
num_range=np.arange(1,11,2)
print(numbers_arr)
print(num_range)

#ZEROS AND ONES

n1=np.zeros([3,3],dtype='int32')
print("Matrix filled with zeros:",'\n',n1)

n2=np.ones([10,10],dtype='int32')
print("Matrix filled with ones:",'\n',n2)

#LINSPACE

n1=np.linspace(1,11,25)

print(n1)

#IDENTITY MATRIX
num=int(4)
matrix=np.identity(num,dtype='int')
print(matrix)


#RANDOM PACKAGE

num1=np.random.uniform(0,1,size=4)
print(num1)

#RAND

#Program 1

num=np.random.randn(2)
print(num)

#program 2

matrix=np.random.randn(6,6)
print(matrix)

#RANDINT

num=np.random.randint(1,6,size=10)
print(num)

#ARRAY AND ATTRIBUTES

#ARRAY

numbers=np.arange(25)
print(numbers)

#RANDOM

ran_int=np.random.randint(0,50,size=10)
print("10 random integer:",ran_int)

#SHAPE

a=np.array([[1,2,3],[4,5,6]])
print("a:",a)
print("Shape of array a:",a.shape)

#RESHAPE

a=np.array([1,2,3,4,5,6])
print(a.reshape(2,3))

#MINIMUM

num=np.array([3,4,8,2,9])
print("numbers:",num)
print("Minimum nuber in array:",min(num))

#TASK 3

#ARGUMENT FUNCTION

r=np.array([1,2,3,4,5])
index=np.argmax(r)
print("Index of maximum value of array:",index)

#SLICING

a=np.array([1,2,3,4,5,6,7,8,9,10])
a[:5]=1000
print(a)

#INDEXING

mat=np.array([1,2,3,4,5,6,7,8,9])
print(mat.reshape(3,3))

#ARITHMETIC OPERATORS

c=np.arange(1,11)
print("Array:",c)

print("Addition:",c+c)
print("Subraction:",c-c)
print("Multiplication:",c*c)
print("Division:",c/c)

#UNIVERSAL ARRAY

a=np.arange(1,11)
b=np.arange(1,11)
print("a:",a)
print("b:",b)

print("Addition:",a+b)
print("Subraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)

#TRIGONOMETRIC FUNCTION

angle_value=np.array([0,np.pi/2,np.pi,np.pi*3/2,np.pi*2])
sine_values = np.sin(angle_value)
cosine_values = np.cos(angle_value)
print("sine value:",sine_values)
print("cosine value:",cosine_values )


#EXPONENTIATION OF ARRAY ELEMENTS

'n=np.array([5,4,5,9,8,3])
expo=2
print(np.power(n,expo))

#SQUARE ROOT

a=np.array([4,9,16,25,32])
print(np.sqrt(a).astype(int))

#MATRIX MULTIPLICATION

mat=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat*mat)


































































































