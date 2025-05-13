#program 1

def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Zero division error")
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
result=safe_divide(a,b)
print(result)

#program 2
try:
    number=int(input("Enter a number1:"))
    text=input("Enter a number2:")
    convert_text=int(text)
    result=number/convert_text
    print(result)
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("can't divide by zero")
#program 3

def demo():
    try:
        file=open("data.txt","r")
        content=file.read()
        print(content)
    except Exception as e:
        print("something wrong")
    finally:
        file.close()
    
demo()

#program 4

class AgeError(Exception):
    pass
def age_error():
    try:
        age=int(input("Enter your age:"))
        if age<18:
             raise AgeError("You must be atleast 18 years old.")
        else:
            print("you can enter successfully.")
    except ValueError:
        print("Invalid input,please enter numbers only.")
        
age_error()


#program 5

try:
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
    div=num1/num2
    print(div)
except ZeroDivisionError:
    print("can't divide by zero.")
except ValueError:
    print("Invalid input,please enter intergers only.")
else:
    print("operation Successful.")

#program 6
import string
alpha=list(string.ascii_letters)
password=input("Enter the password:")
def validate_password(password):
    
    emp1=0
    emp2=0
    try:
        if len(password)<8:
                raise ValueError("The password must be atleast 8 characters.")


        for i in password:
            if i in alpha:
                emp1=emp1+1
            if i not in alpha:
                emp2=emp2+1
        if emp1<1 or emp2<1:
            raise ValueError("The password must contain both letters and numbers.")
        else:
            print("Your password:",password)
    except ValueError as e:
         print("Error:",e)

validate_password(password)

#program 7
def error_log():
    
    try:
        file=open("log_error.txt","a+")
        num1=int(input("Enter a number:"))
        num2=int(input("Enter a number:"))
        div=num1/num2
        print(div)
    except ZeroDivisionError:
        file.write("can't divide by zero.")
    except ValueError:
        file.write("Invalid input,please enter intergers only.")
    else:
        file.write("operation Successful.")
        
error_log()

#program 8

def outer_function():
    def inner_function(a,b):
        return a/b      
    try:
        a=int(input("Enter a number:"))
        b=int(input("Enter a number:"))
        inner_function(a,b)
    except ZeroDivisionError:
        print("can't divide by zero")
    
      
outer_function()

#program 9

def read_file(filename):
    try:
        with open(filename,"r") as file:
            content=file.read()
            print(content)
    except FileNotFoundError:
        print("file does not exist")
    
filename=input("Enter the file name:")

read_file(filename)

#program 10
try:
    num1=input("Enter a number:")
    num2=int(num1)
    print("Success you enter the number.",num2)
except Exception:
    print("Invalid input")

#program 11

name=input("Enter your name:")
age=int(input("Enter your age:"))
print(f"Hello {name},you are {age} years old!")


#program 12

def decimal_places():
    number=float(input("Enter the number:"))
    print("Using F_string formatting:",f"{number:.2f}")
    result=format(number,".2f")
    print("Using format() formatting:",result)
decimal_places() 

#program 13

items=[("Pen",10),("Pencil",15),("Scale",5),("Eraser",8)]
item_width=10
price_width=10
print("Item".ljust(item_width)+"|"+"price".rjust(price_width))
print("-"*(item_width+price_width))
for item,price in items:
    print(item.ljust(item_width) +"|"+ f"Rs.{price}".rjust(price_width))



#program 14

person={"name":"John","age":30,"city":"New York"}

result="{} is {} old and lives in {}.".format(person["name"],person["age"],person["city"])
print(result)

#program 15

number=int(input("Enter the number:"))
res="{:,}".format(number)
print(res)

#progrm 16

import string
alpha=list(string.ascii_letters)
password=input("Enter the password:")
def validate_password(password):
    
    emp1=0
    emp2=0
    try:
        if len(password)<8:
                raise ValueError(f"The password {password} is too short.It must be atleast 8 characters.")


        for i in password:
            if i in alpha:
                emp1=emp1+1
            if i not in alpha:
                emp2=emp2+1
        if emp1<1 or emp2<1:
            raise ValueError("The password must contain both letters and numbers.")
        else:
            print("Your password:",password)
    except ValueError as e:
         print("Error:",e)

validate_password(password)



#program 17

import datetime
date_time=datetime.datetime.now()
today_date=date_time.strftime("%B %d %Y")
current_time=date_time.strftime("%I:%M %p")
print(f"Today is {today_date}, and the time is {current_time}")

#program 18

name=input("Enter your name:")
age=int(input("Enter your age:"))
email=input("Enter your email:")
print(f"""
name: {name}
age: {age}
email: {email}""".format(name,age,email))


#program 19
def create_file():
    file=open("student.txt","w+") 
    file.write("1.raj\n2.rohit\n3.allu")
    file.seek(0)
    content=file.read()
    print(content)
    file.close()
create_file()

#program 20

def read_and_append(filename,text):
    file=open(filename,"a+")
    file.write('\n'+text)
    file.seek(0)
    content=file.read()
    print("Updated content:",content)    
    
filename=input("Enter the file name:")
text=input("Enter a text that add into the file:")
read_and_append(filename,text)
