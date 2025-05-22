import ast
import locale
student={}
def add_student():
        emp_set=set()
        try:
                with open("students.txt","r")as file:
                        lines=file.readlines()
                        for line in lines:
                                user_id,details=line.strip().split(":",1)
                                student_data=ast.literal_eval(details)
                                emp_set.add(user_id)
        except FileNotFoundError:
                print("File Not Found")
        while True:
                try:
                        student_id=input("Enter your id:")
                        if student_id.isalpha():
                                raise ValueError("Invalid Input")

                        if student_id in emp_set:
                                print("This studentd Id is already taken.")
                        else:
                                break
                
                except ValueError as e:
                   print("Error",e)
           
        while True:
                name=input("Enter your name:")
                try:
                        if name.isdigit():
                            raise ValueError("Invalid Input")
                        break
                except ValueError as e:
                        print("Error",e)
        while True:
                try:    
                        age=(input("Enter your age:"))
                        if age.isalpha():
                            raise ValueError("Invalid Input")
                        break
                except ValueError as e:
                        print("Error",e)                
        courses_avaliable={"Python","Data Science","Web Development","AI&ML"}
        for index,course in enumerate(courses_avaliable,start=1):
                print(index,course)
        dict_course={'python':'15000','data science':'45000',
                'web development':'50000','ai&ml':'75000'}
        course_enrolled=(input("Enter the course you enrolled:")).lower()
                
        total_fees=dict_course[course_enrolled]
        if course_enrolled not in dict_course:
                print("Invalid course is selected.")
        print("Total Fees:",total_fees)

        fees_paid=int(input("Amount you paid:"))
        balance_amount=(int(total_fees))-(fees_paid)
        print("Balance Amount:",balance_amount)
        student[student_id]={"Name":name,
                         "Age":age,
                         "Course enrolled":course_enrolled,
                         "Total Fees":total_fees,
                         "Fees paid":fees_paid,
                         "Balance Amount":balance_amount}
            
        with open("students.txt","a+")as file:
                file.write(f"{student_id}:{student[student_id]}\n")
            
            
            
        
        


def update_student():
        update_id=int(input("Enter Id:"))
        updated=[]
        update=False
        try:
                with open("students.txt","r") as file:
                        lines=file.readlines()
                        for line in lines:
                                user_id,details=line.strip().split(":",1)
                                student_detail=ast.literal_eval(details)

                                
                                if update_id==int(user_id):
                                        print("1. Update Name")
                                        print("2. Update Age")
                                        print("3. Update Course")
                                        print("4. Update Paid Fees")


                                        user_update=int(input("Enter Value u want to update:"))
                                        if user_update==1:
                                                student_detail["Name"]=input("Enter Name to update:")
                                        elif user_update==2:
                                                student_detail["Age"]=int(input("enter Age to update:"))
                                        elif user_update==3:
                                                        student_detail["Course enrolled"]=input("Enter Course to update:")
                                        elif user_update==4:
                                                student_detail["Fees paid"]=int(input("Enter the amount y have been paid:"))
                                                student_detail["Balance Amount"]=student_detail["Total Fees"]-student_detail["Fees paid"]
                                                print(f"Balance Amount is:",student_detail["Balance Amount"])
                                update=True
                                updated.append(f"{user_id}:{str(student_detail)}\n")
                                        
                                        

                with open("students.txt","w") as file:
                        for line in updated:
                                file.writelines(line)
                if update:
                        print("File successfully Updated")
                else:
                        print("File Not Updated")
        except Exception as e:
                print("error",e)



def remove_student():
        remove_id=int(input("Enter Id:"))
        add_value=[]
        remove=False
        with open("students.txt","r")as file:
                lines=file.readlines()
        for line in lines:
                user_id,details=line.strip().split(":",1)
                student_detail=ast.literal_eval(details)
                if remove_id==int(user_id):
                        remove=True
                        continue
                else:
                        add_value.append(f"{user_id}:{str(student_detail)}\n")
                
        
        with open("students.txt","w")as file:
                file.writelines(add_value)
        if remove:
                print("removed Successfully.")
        else:
                print("Student Id Not Found.")



def view_student():
        with open("students.txt","r")as file:
                content=file.read()
                file.seek(0)
                print(content)


def generate_fees():
        fees_generated=False
        with open("students.txt","r")as file:
                lines=file.readlines()   #stored as a string
                for line in lines:
                        student_id,details=line.strip().split(":",1)
                        student_data=ast.literal_eval(details)    #convert into dict
                        if student_data["Fees paid"]>0:
                                fees_generated=True
                                print(f"Student Id:{student_id}")
                                print(f"student Name:{student_data["Name"]}")
                                print(f"Course Enrolled:{student_data["Course enrolled"]}")
                                print(f"Balance Amount:{student_data["Balance Amount"]}")
                                
                        
                        else:        
                                print("Student doesn't have balance amount")
        
        
        
        
                                

                                        

while True:
        print("1. Add Student")
        print("2. Update Student")
        print("3. Remove Student")
        print("4. View Student")
        print("5. Generate Fees")
        print("6. Exit")


        choice=int(input("Enter Choice:"))
        if choice==1:
                add_student()
        elif choice==2:
                update_student()
        elif choice==3:
                remove_student()
        elif choice==4:
                view_student()
        elif choice==5:
                generate_fees()
        elif choice==6:
                break
        else:
                pass




























        
        










