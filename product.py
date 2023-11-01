from utility import *

class Product:
    def __init__(self):
        pass
        
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
      
    def display_products(self):
        with open(productsFilePath, "r") as file:
            print("Available Products:")
            for i, line in enumerate(file, start=1):
                if(line.strip() != None):
                    print(f"\t{i}. {line.strip()}")
                else:
                    print("\tNo products available")
                    break
                


    def checkout_product(self, product_id, name, price, quantity, category):
        order_data = f"{self.product_id}|{product_id}|{name}|{price}|{quantity}|{category}\n"
        with open(ordersFilePath, "a") as file:
            file.write(order_data)
            print(f"Ordered {quantity} of {name} for customer {self.product_id}")