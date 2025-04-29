#program 1
for i in range(1,11):
    print(i)

#program 2
for i in range(1,20+1):
    if i%2==0:
        print(i)

#program 3
for i in range(1,20+1):
    if i%2!=0:
        print(i)

#program 4
num=5
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)

#program 5
count=0
for i in range(1,100+1):
    count=count+i
print(count)

#program 6
num=[1,2,3,4,5]
count=0
length=len(num)
for i in num:
    count=count+i
result=count/length
print(result)

#program 7
for i in range(1,4):
    for j in range(1,4):
        print("*",end=" ")
    print()                  

#program 8
for i in range(1,6):
    print(i)

#progarm 9
for i in range(1,11):
    print(i)


#program 10
list=[10,20,30,40,10]
if list[0]==list[-1]:
    print("True")

#program 11
list=[10,8,15,5,9]
emp=[]
for i in list:
    if i%5==0:
        emp.append(i)

print("Numbers divisible by 5 in the list:",emp)

#program 12
n=input("Enter the alphabet:")
list=['a','e','i','o','u']
if n in list:
    print("The alphabet is vowels:")        
else:
    print("The alphabet is consonants")

#program 13
num1=10
num2=55

counteven=0
countodd=0
for i in range(num1,num2):
    if i%2==0:
        counteven=counteven+1
    else:
        countodd=countodd+1
        
print(counteven)
print(countodd)

#program 14
for i in range(1,26):
    if i%5!=0:
        print(i)


#program 15
list=[1,2,3,4]
fact=1
for i in list:
        fact=fact*i
        print(fact)
        


#program 16
num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))
product=num1*num2
print("product:",product)
if product>500:
    print("Sum:",num1+num2)


#program 17
num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))
if num1>num2:
    print("Number1 is greater than number2")
else:
    print("Number2 is greater than number1")

#program 18
num1=int(input("Enter numbrer1:"))
num2=int(input("Enter number2:"))
num3=int(input("Enter number3:"))
if num1>num2 and num1>num3:
    print("number1 is greater")
elif num2>num3:
    print("Number2 is greater")
else:
    print("Number3 is greater")

#program 19
list=[23,4,-6,23,-9,21,3,-45,-8]
list1=[]
list2=[]
for i in list:
    if i<0:
        list1.append(i)
    elif i>0:
        list2.append(i)
print(list1)
print(list2)


































    














        





















































    
    
    
