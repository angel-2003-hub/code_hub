#program 1
num1=int(input("enter the number1:"))
num2=int(input("Enter the number2:"))
product=num1*num2
if (product>500):
    print("sum of the number:",num1+num2)
else:
    print("Product of the number:",product)


#program 2
num1=2
num2=8
num3=15
if(num1>num2 & num1>num3):
    print("the greater number is:",num1)
elif(num2>num1 & num2>num3):
    print("The greater number is:",num2)
else:
    print("the greater number is:",num3)

#program 3
list=[12,34,76,34,44]
first=[]
for i in list:
    if i not in first:
        first.append(i)
print(first)


#program 4
nums=[3,2,2,3]
list=[]
for i in nums:
    if i==2:
        list.append(i)
while len(list)<len(nums):
        list.append("_")
print(list)



#program 5
nums=[1,2,3,1]
list=[]
for i in nums:
    if i not in list:
        list.append(i)
if len(list)<len(nums):
    print("true")
else:
    print("False")
        
#program 6
num=38
while num>=10:
    temp=0
    while num>0:
        n=num%10  #8
        temp=temp+n    #8+3
        num=num//10
    num=temp   #11     2
print(num)



#program 7
num=[1,0,2,3,0,4,5,0]
num1=num.copy()
length=len(num)
for position,i in enumerate(num1.copy()):
    if i==0:
        num1.insert(position+1,0)
    if len(num1)>length:
        num1.pop()
print(num1)
        


#program 8
num1=[1,2,2,1]
num2=[2,2]
set1=set(num1)
set2=set(num2)
result=set1.intersection(set2)
print(list(result))
    











        
    
    
    


























        
