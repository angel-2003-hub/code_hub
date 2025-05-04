'''#program 1
def demo(a):
    return (pow(a,3))
a=int(input("Enter a number:"))

result=demo(a)
print(result)'''


#program 2
while True:
    num=int(input("Enter the number:"))
    if num<0:
        break
    else:
        print(pow(num,3))

'''#program 3
for i in range(1,21):
    if i%2!=0:
        continue
    else:
        print(i)

#program 4
sum=0
while True:
    
        num=int(input("Enter the number:"))
        if num<0:
            continue
        elif num==0:
            break
        else:
                sum=sum+num
                print(sum)
        
            

#program 5
def scope():
        num=10
        print("Square of numbers:",num*num)

#sum=num+1
#print(sum)
scope()



#program 6
def scope():
        global counter
        counter=counter+1
        print(counter)
counter=10

scope()
scope()
scope()

#program 7
def scope():
        global x
        x=10
        print("x:",x)
x=5
def new_scope():
        y=15
        print("y:",y)
scope()
new_scope()

#program 8
fruits=('apple','banana','cherry')
print(fruits[1])
fruits_list=list(fruits)
fruits_list[1]='orange'
print(fruits_list)
print(tuple(fruits_list))

#program 9
set1={1,2,3,4,5}
set2={4,2,6,8,1}
print("intersection:",set1.intersection(set2))
print("union:",set1.union(set2))
print("Difference:",set1.difference(set2))
set1.add(10)
print(set1)
set2.remove(4)
print(set2)
if 5 in set1:
        print("The element present in set1")
else:
        print("The element not in the set1")


#program 10
numbers=(5,7,8,10,12,18)
print(numbers[2])
set1=set(numbers)

set1.add(21)
print(set1)

#program 11
org_list=[1,2,4,7,9,1,7]
set1=set(org_list)
print(set1)
set2={9,8,7,6,5}
emp_list=[]
for i in org_list:
        if i not in emp_list:
                emp_list.append(i)
print("uniqe elements from the orginial list:",emp_list)
print("Intersection of set1 and set2:",set1.intersection(set2))
print("Union of set1 and set2:",set1.union(set2))

#program 12
num_list=[10,20,30,40,50]
num_list.append(60)
print(num_list)
print(tuple(num_list))
print(set(num_list))'''

