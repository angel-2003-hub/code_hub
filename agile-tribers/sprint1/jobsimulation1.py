import random
while True:
    length=int(input("Enter the password length you needed:"))
    if length<0:
        print("The length must be greater than zero")
    elif length>0 and length<8:
        print("The password should be atleast 8 character")
    else:
        break

letter=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
numbers=list('1,2,3,4,6,5,7,8,9,0')
splchar=['!','@','$','<','>','.','%','^','&','*','(',')','_','-','+','#']
merge=letter+numbers+splchar

stored=random.sample(merge,length)

remove_quote=''.join(stored)


print(remove_quote)

