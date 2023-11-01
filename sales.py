from utility import *

class FinancialReport:
    def __init__(self, ordersFilePath, expenditureFilePath, productsFilePath):
        self.ordersFilePath = ordersFilePath
        self.expenditureFilePath = expenditureFilePath
        self.productsFilePath = productsFilePath

    def calculate_total_revenue(self):
        total_revenue = 0
        with open(self.ordersFilePath, "r") as file:
            for line in file:
                data = line.strip().split('|')
                price = float(data[3])
                quantity = int(data[4])
                total_revenue += price * quantity
        return total_revenue

    def calculate_total_expenditure(self):
        total_expenditure = 0
        with open(self.expenditureFilePath, "r") as file:
            for line in file:
                expenditure = float(line.strip())
                total_expenditure += expenditure
        return total_expenditure

    def calculate_total_products(self):
        total_products = 0
        with open(self.productsFilePath, "r") as file:
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

report = FinancialReport(ordersFilePath, expenditureFilePath, productsFilePath)
report.generate_report()
