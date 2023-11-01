from datetime import datetime
# import datetime
from person import Person
from utility import *

class Employee(Person):
    def __init__(self) -> None:
        super().__init__()
        
    def CreateExpenditure(self,purpose,amount):
        self.purpose = purpose
        self.amount = amount
        current_date = datetime.date.today()
        expenditureString = f"{self.purpose}|{self.amount}|{current_date}"
        f = open(expenditureFilePath,'a')
        f.write(expenditureString+"\n")
        print("Expenditure Created!")
        
    def CreateCoupon(self,couponCode,percent,expiryDate):
        self.couponCode = couponCode
        self.percent = percent
        self.expiryDate = expiryDate
        couponString = f"{couponCode}|{percent}|{expiryDate}"
        f = open(couponsFilePath,'a')
        f.write(couponString+"\n")
        print("Coupon Created!")
        
    def ClearAllExpiredCoupon(self):
        with open(couponsFilePath, 'r') as file:
            lines = file.readlines()

        modified_lines = []
        found = False
        for line in lines:
            couponInfo = line.strip().split('|')
            if line == "\n":
                continue
            else:
                if "\n" not in line:
                    line = line + "\n"
            if len(couponInfo) > 0:
                given_date = datetime.strptime(couponInfo[2], "%Y-%m-%d")
                current_date = datetime.today()
                if(given_date >= current_date):
                    modified_lines.append(line)
                    
        with open(couponsFilePath, 'w') as file:
            file.writelines(modified_lines)
            
        print("All Expired Coupons Are Cleared!")
        

        
        
        