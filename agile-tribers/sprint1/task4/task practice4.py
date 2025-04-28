#program 1
num=int(input("enter the number:"))
if(num>0):
    print("The number is positive")
else:
    print("The number is negative")


#program 2

num=int(input("Enter the number:"))
if num%2==0:
    print("The number is even")
else:
    print("The number is odd") 

#program 3
base=int(input("Enter the base number:"))
exponent=int(input("Enter the power nunmer:"))
power=pow(base,exponent)
print(power)

#program 4
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if num1==num2:
    print("number1 is equal to number2")
elif num1>num2:
    print("number1 greater than number2")
else:
    print("Number2 is greater than number1")

#program 5
year=int(input("Enter the year:"))
if year%4==0:
    print("The year is the leap year")
else:
    print("The year is not a leap year")

#program 6
score=int(input("Enter your score:"))
if score>=90:
    print("your grade is A")
elif score>=80:
    print("rour grade is B")
elif score>=70:
    print("your grade is C")
elif score>=60:
    print("your grade is D")
elif score<60:
    print("your grade is F")

#program 7
age=int(input("Enter your age:"))
if age<16:
    print("you can't drive")
elif age>=16 and age<=17:
    print("you can drive but not vote")
elif age>=18 and age<=24:
    print("you can vote but not rent a car")
elif age>25:
    print("you can do everything")

#program 8
for i in range(1,101):
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
    else:
        print(i)


#program 9
year=int(input("Enter the year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")

        























        

