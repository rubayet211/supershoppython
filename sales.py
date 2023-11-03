from utility import *

class FinancialReport:
    def __init__(self):
        pass

    def calculate_total_revenue(self):
        total_revenue = 0
        with open(ordersFilePath, "r") as file:
            for line in file:
                data = line.strip().split('|')
                price = float(data[6])
                total_revenue += price
        return total_revenue

    def calculate_total_expenditure(self):
        total_expenditure = 0
        with open(expenditureFilePath, "r") as file:
            for line in file:
                data = line.strip().split('|')
                expenditure= float(data[1])
                total_expenditure += expenditure
        return total_expenditure

    def calculate_total_products(self):
        total_products = 0
        with open(productsFilePath, "r") as file:
            for line in file:
                data = line.strip().split('|')
                quantity = int(data[3])
                total_products += quantity
        return total_products

    def generate_report(self):
        total_revenue = self.calculate_total_revenue()
        total_expenditure = self.calculate_total_expenditure()
        total_products = self.calculate_total_products()
        net_profit = total_revenue - total_expenditure

        print(f"Total products available: {total_products}")
        print(f"Total revenue: {total_revenue}")
        print(f"Total expenditure: {total_expenditure}")
        print(f"Net profit: {net_profit}")

