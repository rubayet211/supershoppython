from utility import *

class Product:
    def __init__(self):
        pass
    def EmptyProduct(self):
        emptyProduct = False
        return emptyProduct
        
    def add_product(self,product_id, name, price, quantity, category):
        self.product_id = self.GenerateProductId()
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        new_data = f"{self.product_id}|{self.name}|{self.price}|{self.quantity}|{self.category}\n"
        with open(productsFilePath, "a") as file:
            file.write(new_data)
            print(f"Added {self.name} to {self.category} with price {self.price} and quantity {self.quantity}")

    def update_product(self, new_price, new_quantity):
        self.price = new_price
        self.quantity = new_quantity

        lines = []
        with open(productsFilePath, "r") as file:
            for line in file:
                data = line.strip().split('|')
                if len(data) > 0 and data[0] == self.product_id:
                    line = f"{self.product_id}|{self.name}|{self.price}|{self.quantity}|{self.category}\n"
                lines.append(line)

        with open(productsFilePath, "w") as file:
            file.writelines(lines)
            print(f"Updated {self.name} in {self.category} with new price {self.price} and new quantity {self.quantity}")

    def delete_product(self):
        lines = []
        with open(productsFilePath, "r") as file:
            for line in file:
                data = line.strip().split('|')
                if len(data) > 0 and data[0] != self.product_id:
                    lines.append(line)

        with open(productsFilePath, "w") as file:
            file.writelines(lines)
            print(f"Deleted product with id {self.product_id}")

    def add_quantity(self, quantity):
        self.quantity += quantity
        self.update_product(self.price, self.quantity)

    def substract_quantity(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            self.update_product(self.price, self.quantity)

    def GenerateProductId(self):
        productCnt = 1
        f = open(productsFilePath, "r")
        
        for line in f:
            productCnt += 1
        product_Id = f"Product-{productCnt}"
        return product_Id


    def deduct_product_quantity(self, product_id, quantity_ordered):
        with open(productsFilePath, "r") as file:
            products = file.readlines()

        with open(productsFilePath, "w") as file:
            for product in products:
                data = product.strip().split('|')
                if data[0] == product_id:
                    data[3] = str(int(data[3]) - int(quantity_ordered))
                file.write("|".join(data) + "\n")



    def checkout_product(self, product_id, name, price, quantity, category, customer_id):
        import customer
        c = customer.Customer()
        order_data = f"{product_id}|{name}|{price}|{quantity}|{category}|{customer_id}\n"
        with open(ordersFilePath, "a") as file:
            file.write(order_data)
            print(f"Customer-{customer_id} purchased {quantity} of {name}")
            self.deduct_product_quantity(product_id, quantity)

    
    def BrowseRegister(self):
        import customer
        c = customer.Customer()
        customerName=input("Enter your name: ")
        customerPhone=input("Enter your phone number: ")
        customerAddress=input("Enter your address: ")
        customerDob=input("Enter your date of birth: ")
        c.register_customer(customerName,customerPhone,customerAddress,customerDob)
        return c.customer_id


    def order_product(self):
        import customer
        c = customer.Customer()
        with open(productsFilePath, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No products available")
                return
            else:
                print("Available Products:")
                products = []
                for i, line in enumerate(lines, start=1):
                    data = line.strip().split('|')
                    if len(data) > 4:
                        print(f"\t{i}. Category: {data[4]}, Product Name: {data[1]}, Price: {data[2]}, Stock: {data[3]}")
                        products.append(data)
                product_id = int(input("Enter the number of the product you want to order: ")) - 1
                quantity = int(input("Enter the quantity you want to order: "))
                if quantity > int(products[product_id][3]):
                    print("Not enough stock")
                    return
                else:
                    print("Do you have coupon code?")
                    print("1. Yes")
                    print("2. No")
                    couponChoice = int(input("Enter your choice: "))
                    if couponChoice == 1:
                        couponCode = input("Enter Coupon Code : ")
                        c.ApplyCoupon(couponCode)
                        print("Register or Login to proceed to checkout:")
                        print("1. Login")
                        print("2. Register")
                        print("3. Exit")
                        choice = int(input("Enter your choice: "))
                        if choice == 1:
                            uniqueID = input("Enter your Unique Login ID: ")
                            customer_id=c.Login(uniqueID)
                            self.checkout_product(products[product_id][0], products[product_id][1], products[product_id][2], quantity, products[product_id][4], customer_id)
                        elif choice == 2:
                            customer_id = self.BrowseRegister()
                            self.checkout_product(products[product_id][0], products[product_id][1], products[product_id][2], quantity, products[product_id][4], customer_id)
                        elif choice == 3:
                            return
                        else:
                            print("Invalid choice")
                            return
                    elif couponChoice == 2:
                        print("Register or Login to proceed to checkout:")
                        print("1. Login")
                        print("2. Register")
                        print("3. Exit")
                        choice = int(input("Enter your choice: "))
                        if choice == 1:
                            uniqueID = input("Enter your Unique Login ID: ")
                            customer_id=c.Login(uniqueID)
                            self.checkout_product(products[product_id][0], products[product_id][1], products[product_id][2], quantity, products[product_id][4], customer_id)
                        elif choice == 2:
                            customer_id = self.BrowseRegister()
                            self.checkout_product(products[product_id][0], products[product_id][1], products[product_id][2], quantity, products[product_id][4], customer_id)
                        elif choice == 3:
                            return
                        else:
                            print("Invalid choice")
                            return
    
    



    