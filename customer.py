from person import Person
from product import Product
from utility import *
import random

showProduct = Product()

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

    def generate_customer_id(self):
        with open(userFilePath, "r") as file:
            lines = file.readlines()
        customer_id = random.randint(1, 10000)
        return customer_id

    def BuyProducts(self, customer_id, product_id, name, price, quantity, category):
        order_data = f"{self.customer_id}|{product_id}|{name}|{price}|{quantity}|{category}\n"
        with open(ordersFilePath, "a") as file:
            file.write(order_data)
            print(f"Ordered {quantity} of {name} for customer {self.customer_id}")


    def UpdateProfile(self, name, password, salary):
        # Implement profile update logic here
        # Update the customer's profile information
        self.name = name
        self.password = password
        self.salary = salary
        # Save the updated profile to the user file
        user_info = f"{self.user_id}|{self.password}|{self.name}|{self.join_date}|{self.salary}\n"
        with open(userFilePath, "a") as file:
            file.write(user_info)

    def ViewProfile(self):
        # Implement profile view logic here
        # Display the customer's profile information
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        # You can add more profile information to display

    def DeleteProfile(self):
        # Implement profile deletion logic here
        # Remove the customer's profile from the user file
        with open(userFilePath, "r") as file:
            users = file.readlines()

        with open(userFilePath, "w") as file:
            for user in users:
                user_info = user.split('|')
                if user_info[0] != self.user_id:
                    file.write(user)

    def ApplyCoupon(self, coupon_code):
        # Implement coupon application logic here
        # Check if the provided coupon code is valid
        with open(couponsFilePath, "r") as file:
            coupons = file.readlines()

        applied_discount = 0
        for coupon in coupons:
            coupon_info = coupon.split('|')
            if coupon_info[0] == coupon_code:
                applied_discount = float(coupon_info[1])
                break

        # Apply the applicable discount to the order total
        with open(ordersFilePath, "r") as file:
            orders = file.readlines()

        with open(ordersFilePath, "w") as file:
            for order in orders:
                order_info = order.split('|')
                if order_info[0] == self.customer_id:
                    order_price = float(order_info[3])
                    order_quantity = int(order_info[4])
                    total_price = order_price * order_quantity
                    discounted_price = total_price - (total_price * applied_discount / 100)
                    order_info[3] = str(discounted_price)
                file.write("|".join(order_info))

        print(f"Applied {applied_discount}% discount using coupon {coupon_code}")

    def ViewOrders(self):
        # Implement order view logic here
        # Display the customer's orders
        with open(ordersFilePath, "r") as file:
            orders = file.readlines()

        print("Orders:")
        for order in orders:
            order_info = order.split('|')
            if order_info[0] == self.customer_id:
                print(f"Product: {order_info[2]}, Quantity: {order_info[4]}, Price: {order_info[3]}")
    

    def Login(self, customer_id):
        with open(userFilePath, "r") as file:
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
        else:
            print("Invalid customer ID")
            return False
