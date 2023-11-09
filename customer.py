from person import Person
from utility import *
import random


class Customer(Person):
    def __init__(self)->None:
        super().__init__()

    
    def register_customer(self, name, phone_number, address, dob):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.dob = dob
        self.customer_id = self.generate_customer_id()
        customer_info = f"{self.customer_id}|{self.name}|{self.phone_number}|{self.address}|{self.dob}\n"
        with open(customerInfoPath, "a") as file:
            file.write(customer_info)
        print(f"Customer {self.name} registered successfully with ID {self.customer_id}")
        return self.customer_id

    def generate_customer_id(self):
        with open(customerInfoPath, "r") as file:
            lines = file.readlines()
        customer_id = random.randint(1, 10000)
        return customer_id


    def ApplyCoupon(self, coupon_code, total_price):
        with open(couponsFilePath, "r") as file:
            coupons = file.readlines()

        applied_discount = 0
        for coupon in coupons:
            coupon_info = coupon.split('|')
            if coupon_info[0] == coupon_code:
                applied_discount = float(coupon_info[1])
                break
        discounted_price = total_price - (total_price * applied_discount / 100)
        print(f"Applied {applied_discount}% discount on Total Price-{total_price} using coupon {coupon_code}")
        return discounted_price

    
    def Login(self, customer_id):
        with open(customerInfoPath, "r") as file:
            users = file.readlines()
        is_valid = False
        for user in users:
            user_info = user.split('|')
            if user_info[0] == customer_id:
                is_valid = True
                break
        if is_valid:
            self.customer_id = customer_id
            print(f"Customer {self.customer_id} logged in successfully")
            return customer_id
        else:
            print("Invalid customer ID")
            return False
        
    def viewCustomer(self,customer_id):
        with open(customerInfoPath, "r") as file:
            users = file.readlines()
        is_valid = False
        for user in users:
            user_info = user.split('|')
            if user_info[0] == customer_id:
                print(f"Customer ID: {user_info[0]}")
                print(f"Name: {user_info[1]}")
                print(f"Phone Number: {user_info[2]}")
                print(f"Address: {user_info[3]}")
                print(f"DOB: {user_info[4]}")
                is_valid = True
                break
        if not is_valid:
            print("Invalid customer ID")

        
