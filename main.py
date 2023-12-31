from person import Person
from admin import Admin
from product import Product
from utility import *
from employee import *
from customer import *
from sales import *
import os
import sys

def option():
    print("\n### Press any option and hit enter ###")
def MainMenu():
    os.system('cls')
    option()
    print("1. Browse Products")
    print("2. Login")
    print("3. Exit")

def LoginOption():
    os.system('cls')
    option()
    print("1. login as Admin")
    print("2. login as Employee")
    print("3. Back")
    
def AdminShowMenu():
    os.system('cls')
    option()
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. My Profile")
    print("5. View Sales")
    print("6. View a Customer")
    
def EmployeeShowMenu():
    os.system('cls')
    option()
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Add Expenditure")
    print("5. Add Coupon")
    print("6. Clear All Expired Coupon")
    print("7. My Profile")
    print("8. View a Customer")
    print("9. Back")
    
    
def UpdateEmployeeMenu():
    os.system('cls')
    option()
    print("1. Update Name")
    print("2. Update Password")
    print("3. Update Salary")
    print("4. Back")
    
def UpdateProductMenu():
    os.system('cls')
    option()
    print("1. Update Product Name")
    print("2. Update Product Quantity")
    print("3. Update product Category")
    print("4. Update product Price")
    print("5. Back")
        
def pause():
    print("Press any key to continue!")
    input()
    

admin = Admin()
employee = Employee()
product = Product()
customer = Customer()
report = FinancialReport()
MainMenu()
userInput=0

def MainMenuInput():
    min_num = 1
    max_num = 3

    while True:
        try:
            global userInput
            userInput = int(input(f"Enter an option between {min_num} and {max_num}: "))
            if min_num <= userInput <= max_num:
                break 
            else:
                print("Input is not between the specified range. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def Login():
    if userInput == 3:
        sys.exit()
    if userInput == 2:
        LoginOption()
        while True:
            choice = input("Enter your choice: ")

            if choice == '1': 

                userId = input("Enter UserId: ")
                password = input("Enter Password: ")
                if admin.Auth(userId,password) == True:
                    while True:
                        AdminShowMenu()
                        try:
                            option = int(input("Enter your choice: "))
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                        if option == 7:
                            break
                        elif option == 1: 
                            empName = input("Employee Name : ")
                            empPassword = input("Employee Password : ")
                            empSalary = input("Employee Salary : ")
                            admin.AddingEmployee(empName,empPassword,empSalary)
                            print("Employee Added!!!")
                            pause()
                        elif option == 2:
                            empUserId = input("Enter employee userId you want to update: ")
                            f = open(userFilePath, "r")
                            foundEmp = False                      
                            for emp in f:
                                empInfo = emp.split('|')
                                if empInfo[0] == empUserId and "emp" in empInfo[0]:
                                    foundEmp = True
                                    UpdateEmployeeMenu()
                                    print(f"Name : {empInfo[2]}")
                                    print(f"User Id : {empInfo[0]}")
                                    print(f"Password : {empInfo[1]}")
                                    print(f"Date Joined : {empInfo[3]}")
                                    print(f"Salary : {empInfo[4]}")
                                    
                                    try:
                                        op = int(input("Enter Option : "))
                                        if op == 1:
                                            empName = input("Enter New Name : ")
                                            empInfo[2] = empName 
                                        elif op == 2:
                                            empPassword = input("Enter New Password : ")
                                            empInfo[1] = empPassword
                                        elif op == 3:
                                            empSalary = input("Enter New Salary : ")
                                            empInfo[4] = empSalary
                                    except ValueError:
                                        print("Please press only integer options!")
                                    empInfoString = '|'.join(empInfo)
                                    admin.UpdatingEmployee(userFilePath,empInfo[0],empInfoString)
                            if foundEmp == False:
                                print("No Employee Found!!")
                                pause()
                        elif option == 3: 
                            empUserId = input("Enter employee userId you want to delete: ")
                            if(admin.DeletingEmployee(userFilePath,empUserId)):
                                print(f"{empUserId} is deleted successfully!!")
                            else:
                                print(f"{empUserId} not found!!")
                            pause()
                        elif option == 4: 
                            admin.MyProfile(userId)
                            pause()
                        elif option == 5: 
                            print("View Financial Report")
                            report.generate_report()
                            pause()
                        elif option == 6:
                            checkCustomer= input("Enter Customer Id : ")
                            customer.viewCustomer(checkCustomer) 
                            pause()               
                                         
                else: 
                    pause()
                    Login()
                break
            elif choice == '2':
                userId = input("Enter UserId: ")
                password = input("Enter Password: ")
                if employee.Auth(userId,password) == True:
                    while True:
                        EmployeeShowMenu()
                        option = int(input("Enter your choice: "))
                        if option == 9: 
                            break
                        elif option == 1: 
                            productName = input("Enter Product Name : ")
                            productPrice = input("Enter Price : ")
                            productQuantity = input("Enter Quantity : ")
                            productCategory = input("Enter Product Category : ")
                            productId = product.GenerateProductId()
                            product.add_product(productId,productName,productPrice,productQuantity,productCategory)
                            pause()
                        elif option == 2:
                            pid = input("Enter Product Id : ")
                            f = open(productsFilePath,'r')
                            for line in f:
                                data = line.split('|')
                                if(data[0] == pid):
                                    while True:
                                        UpdateProductMenu()
                                        op = input("Enter option : ")
                                        if op == '1':
                                            pname = input("Enter Product Name : ")
                                            data[1] = pname
                                            newProductString = '|'.join(data)
                                            product.changeProductName(pid,newProductString)
                                            pause()
                                            break
                                        elif op == '2':
                                            qty = input("Update Quantity : ")
                                            data[3] = qty
                                            newProductString = '|'.join(data)
                                            product.changeProductQuantity(pid,newProductString)
                                            pause()
                                            break
                                        elif op == '3': 
                                            cat = input("Update Category : ")
                                            data[4] = cat
                                            newProductString = '|'.join(data)
                                            product.changeProductCategory(pid,newProductString)
                                            pause()
                                            break
                                        elif op == '4': 
                                            price = input("Update Price : ")
                                            data[2] = price
                                            newProductString = '|'.join(data)
                                            product.changeProductPrice(pid,newProductString)
                                            pause()
                                            break
                                        elif op == '5': 
                                            break
                        elif option == 3: 
                            pid = input("Enter Product Id : ")
                            f = open(productsFilePath,'r')
                            found = False
                            for line in f:
                                data = line.split('|')
                                if(data[0] == pid):
                                    found = True
                                    product.delete_product(pid)
                                    pause()
                            if found == False:
                                print("Product Not Found!!")
                                pause()
                        elif option == 4: 
                            purpose = input("Enter Purpose of Enpense : ")                            
                            amount = input("Enter Amount :  ")          
                            employee.CreateExpenditure(purpose,amount)
                            pause()
                        elif option == 5: 
                            couponCode = input("Enter Coupon Code : ")
                            percent = input("Enter percent of discount : ")
                            expiryDate = input("Enter expiry date (yyyy-mm-dd) : ")
                            employee.CreateCoupon(couponCode,percent,expiryDate)
                            pause()
                        elif option == 6: 
                            employee.ClearAllExpiredCoupon()
                            pause()
                        elif option == 7: 
                            employee.MyProfile(userId)
                            pause()
                        elif option == 8: 
                            checkCustomer= input("Enter Customer Id : ")
                            customer.viewCustomer(checkCustomer) 
                            pause()
                        else:
                            print("Invalid Input!")
                            pause() 
                            
                break
            elif choice == '3':
                print("Logging in as Customer...")
                break
            elif choice == '4':
                print("Going back...")
                break
            else:
                print("Invalid choice. Please select a valid option (1, 2, 3, or 4).")
    if userInput == 1:
        if not product.order_product:  
            print("Exiting program due to no products available.")
            pause()
        else:
            product.order_product()
    else:
        pass

MainMenuInput()
Login()