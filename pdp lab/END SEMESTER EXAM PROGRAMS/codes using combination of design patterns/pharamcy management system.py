from datetime import datetime, timedelta

class Medicine:
    def __init__(self, name, expiry_date, stock_quantity, bin_number):
        self.name = name
        self.expiry_date = expiry_date
        self.stock_quantity = stock_quantity
        self.bin_number = bin_number

    def is_expired(self):
        return datetime.now() > self.expiry_date

    def update_stock(self, quantity):
        self.stock_quantity += quantity

    def __str__(self):
        return f"{self.name} (Bin {self.bin_number}): {self.stock_quantity} in stock, Expires on {self.expiry_date}"

class StockManagement:
    def __init__(self):
        self.medicines = []

    def add_medicine(self, medicine):
        self.medicines.append(medicine)

    def check_stock_availability(self, medicine_name):
        for med in self.medicines:
            if med.name == medicine_name and not med.is_expired() and med.stock_quantity > 0:
                return med
        return None

class SalesManagement:
    def __init__(self, stock_management):
        self.stock_management = stock_management
        self.sales = []

    def generate_invoice(self, prescription):
        invoice = []
        for med_name in prescription:
            medicine = self.stock_management.check_stock_availability(med_name)
            if medicine:
                invoice.append(medicine)
                medicine.update_stock(-1)
                self.sales.append(medicine)
            else:
                print(f"{med_name} is not available or expired.")
        return invoice

class AlertSystem:
    def __init__(self, stock_management, sales_management):
        self.stock_management = stock_management
        self.sales_management = sales_management

    def check_expiry_alerts(self):
        for medicine in self.stock_management.medicines:
            if medicine.is_expired():
                print(f"ALERT: {medicine.name} has expired!")

    def check_low_stock_alerts(self):
        for medicine in self.stock_management.medicines:
            if medicine.stock_quantity < 5:
                print(f"ALERT: Low stock for {medicine.name} (Bin {medicine.bin_number})!")

class OwnerDashboard:
    def __init__(self, sales_management, alert_system):
        self.sales_management = sales_management
        self.alert_system = alert_system

    def display_sales_report(self):
        print("Sales Report:")
        for sale in self.sales_management.sales:
            print(sale)

    def display_stock_report(self):
        print("Stock Report:")
        for medicine in self.sales_management.stock_management.medicines:
            print(medicine)

    def generate_reports(self):
        self.display_sales_report()
        self.display_stock_report()
        self.alert_system.check_expiry_alerts()
        self.alert_system.check_low_stock_alerts()

# Example Usage
if __name__ == "__main__":
    # Create medicines and add them to stock
    med1 = Medicine("Paracetamol", datetime(2024, 1, 15), 50, "A1")
    med2 = Medicine("Aspirin", datetime(2024, 2, 1), 3, "B2")  # Low stock

    stock_manager = StockManagement()
    stock_manager.add_medicine(med1)
    stock_manager.add_medicine(med2)

    # Create SalesManagement instance
    sales_manager = SalesManagement(stock_manager)

    # Create AlertSystem and OwnerDashboard
    alert_system = AlertSystem(stock_manager, sales_manager)
    owner_dashboard = OwnerDashboard(sales_manager, alert_system)

    # Simulate sales
    prescription = ["Paracetamol", "Aspirin", "Ibuprofen"]
    invoice = sales_manager.generate_invoice(prescription)

    # Simulate checking reports and alerts
    owner_dashboard.generate_reports()
