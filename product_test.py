# Import the Product class 
from product import Product
from utility import *

# Display the products in the file
def display_products():
    with open(productsFilePath, "r") as file:
        for line in file:
            print(line.strip())

# Create instances
# product1 = Product("Electronics", "Pendrive", 800, 15)
# product2 = Product("Clothing", "T-Shirt", 1500, 50)
product3 = Product ("Electronics","Pendrive",800,15)
# product4 = Product("Clothing", "Shirt", 2000, 50)

# # Add products to the file
# product1.add_product()
# product2.add_product()
product3.add_product()
# product4.add_product()


# # Display the products before updating
# print("Products before updating:")
# display_products()

# # Update product information
# product1.update_product(850, 6)
# product2.update_product(1800, 45) # Fixed the price value

# # Display the products after updating
# print("\nProducts after updating:")
# display_products()

# # Delete a product
# product1.delete_product()

# Delete a product by specifying its name
# product2.delete_product_by_name("T-Shirt") # Added this line

# Display the products after deleting
# print("\nProducts after deleting:")
# display_products()

# product2.add_quantity(10)

# Display the products after adding quantity
print("\nProducts after adding quantity:")
display_products()
