import datetime
from utility import *

class Person:
    curUser = ""
        
    def __init__(self) -> None:
        pass
            
    def RegisterUser(self,name,password,salary):
        self.name = name
        self.userId = self.GenerateUserId()
        self.password = password
        self.salary = salary
        current_date = datetime.date.today()
        userInfo = f"{self.userId}|{self.password}|{self.name}|{current_date}|{self.salary}"
        f = open(userFilePath, "a")
        f.write(userInfo+"\n")
    
    def Auth(self,userId,password):
        loggedIn = False
        f = open(userFilePath, "r")
        for user in f:
            if len(user) > 0:
                user = user.split('|')
                if user[0] == userId and user[1] == password:
                    self.curUser = userId
        
        if len(self.curUser) == 0:
            print("No such ID/Password Found!!")
        else: 
            print(f"Logged in as {self.curUser}")
            loggedIn = True
        return loggedIn

    
    
    def MyProfile(self,myId):
        f = open(userFilePath,'r')
        found = False
        for user in f:
            if myId in user:
                found = True
                user = user.split('|')
                print("\n#### MY PROFILE ####")
                print(f"Name : {user[2]}")
                print(f"user Id : {user[0]}")
                print(f"Account Opened : {user[3]}")
                if("emp" in user[0]):
                    print(f"Salary : {user[4]}")
        if found == False:
            print("Something went wrong!")

    def UpdatePersonalProfile(self):
        pass
    def ViewSales(self):
        pass
    def ViewSpecificCustomer(self):
        pass
    def UpdateInfo(self,newInfo):
        pass
    
    #support classes
    def GenerateUserId(self):
        f = open(userFilePath, "r")
        
        userId = ""
        userCnt = 1
        for line in f:
            if "emp" in line:
                userCnt += 1
        userId = f"emp-{userCnt}"
        return userId        
        
        
    
    
    
    
    
    
        