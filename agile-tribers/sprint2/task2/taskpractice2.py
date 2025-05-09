#program 1

name={'name':"Alice",'age':25,'city':"New York"}
name["email"]='alice@example.com'
name["age"]=26
del name['city']
print(name)

#program 2

fruit={'apple':10,'banana':5,'cherry':15}
fruit['orange']=8
print("Quantity of banana:",fruit['banana'])
fruit['apple']+=5

del fruit['cherry']
print(fruit)

#program 3


word=input("Enter sentence:")
s_word=word.split()
emp={}
for i in s_word:
    if i not in emp:
        emp[i]=1
    else:
        emp[i]=emp[i]+1
print(emp)

#program 4

#def merge_dicts(dict1,dict2):
dict1={'apple':5,'banana':3,'orange':7}
dict2={'banana':2,'orange':3,'grape':4}
dict3=dict1|dict2

for key,value in dict1.items():
    if key in dict3:
        add=dict3[key]+dict1[key]
        dict3[key]=add
print(dict3)

#program 5

employees={'E001':{'name':'Alice','department':'HR','salary':50000},
           'E002':{'name':'Bob','department':'IT','salary':60000},
           'E003':{'name':'Charlie','department':'Finance','salary':55000}}
def get_salary(employee_dict,emp_id):
    return employee_dict[emp_id]['salary']
def increase_salary(employee_dict,percentage):
    for emp_id in employee_dict:
        increased_salary=employee_dict[emp_id]['salary']
        result=increased_salary*(1+percentage/100)
        employee_dict[emp_id]['salary']=round(result)
      
emp_id=(input("Enter the id:"))
employee_dict=employees
salary=get_salary(employee_dict,emp_id)
print(salary)
percentage=10
increase_salary(employee_dict,percentage)
for emp_id, details in employees.items():
    print(f"{emp_id}: {details}")


#program 6

marks={'Alice':85,'Bob':92,'Charlie':78,'David':90}
sorted_dict=dict(sorted(marks.items(), key=lambda item: item[1], reverse=True))
print(sorted_dict)

#program 7


for i in range(1,11):
    for j in range(1,11):
        print(i*j ,end=" ")
    print()
    

#program 8


Matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
transposed = []

for i in range(len(Matrix[0])):  
    row = []
    for j in range(len(Matrix)):  
        row.append(Matrix[j][i])
    transposed.append(row)

print("Transposed Matrix:", transposed)


    
    
#program 9

prime_count=0
this_list=[[2,4,5],[7,9,11],[13,16,19]]
for row in this_list:
    for num in row:
        count=0
        for i in range(1,num+1):
            
            if num>=2:
                
                if num%i==0:               
                    count=count+1
                
    
        if count<=2:
            prime_count+=1
        
print("The total number of prime number in the list:",prime_count)


#program 10

matrix=[[1,2,3],[4,5,6],[7,8,9]]
emp=[]
emp=emp+matrix.pop(0)
for row in matrix:
    if row:
        emp.append(row.pop())
    if matrix:
        emp.extend(matrix.pop()[::-1])
        emp.extend(matrix.pop()[:])
print(emp)
    

#pogram 11

weight=float(input("Enter the weight:"))
height=float(input("Enter the height:"))
bmi=weight/(height**2)
print(bmi)

if bmi<18.5:
    print("Under Weight")
elif bmi>=18.5 and bmi<24.9:
    print("Over Weight")
elif bmi==25 and bmi<=29.9:
    print("Over Weight")
elif bmi>=30:
    print("Obesity")

#program 12


score=int(input("Enter the score:"))

if score>=90 and score<100:
    print("grade:A")
    print("Status:Pass")
elif score>=80 and score<89:
    print("grade:B")
    print("Status:Pass")
elif score>=70 and score<79:
    print("grade:C")
    print("Status:Pass")
elif score>=60 and score<69:
    print("grade:F")
    print("Status:Fail")
elif score<60:
    print("grade:F")
    print("Status:Fail")

#program 11


matrix=[["madam","apple","racecar"],["level","hello","civic"],["world","deified","rotor"]]

new_list=[]


for i in matrix:
    for j in i:
        word=j[::-1]
        if word==j:
            new_list.append(word)
            print(j,"is palindrome")
        else:
            print(j,"is not palindrome")

        
        

#program 14


for i in range(1,11):
    for j in range(1,11):
        if i%2==0:
            table=i*j
            print(table,end=' ')
    print()

