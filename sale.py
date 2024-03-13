class SaleItem:
    def __init__(self, item_id, name, unit_price):
        self.item_id = item_id
        self.name = name
        self.unit_price = unit_price
    
    def calculate_total(self, quantity):
        raise NotImplementedError("Subclasses must implement calculate_total() method")

class StandardItem(SaleItem):
    def __init__(self, item_id, name, unit_price):
        super().__init__(item_id, name, unit_price)
    
    def calculate_total(self, quantity):
        return self.unit_price * quantity

class DiscountedItem(SaleItem):
    def __init__(self, item_id, name, unit_price, discount_percentage):
        super().__init__(item_id, name, unit_price)
        self.discount_percentage = discount_percentage
    
    def calculate_total(self, quantity):
        total_cost = self.unit_price * quantity
        discount_amount = total_cost * (self.discount_percentage / 100)
        return total_cost - discount_amount

class ServiceItem(SaleItem):
    def __init__(self, item_id, name, hourly_rate):
        super().__init__(item_id, name, hourly_rate)
    
    def calculate_total(self, hours):
        return self.unit_price * hours

# Example usage
if __name__ == "__main__":
    # Standard Item
    standard_item = StandardItem("SI01", "Product A", 10)
    print("Total cost of Standard Item (quantity 8):", standard_item.calculate_total(20))

    # Discounted Item
    discounted_item = DiscountedItem("DI01", "Product B", 30, 10)  # 10% discount
    print("Total cost of Discounted Item (quantity 2):", discounted_item.calculate_total(4))

    # Service Item
    service_item = ServiceItem("SI02", "Service A", 30)  # Ksh 30 per hour
    print("Total cost of Service Item (4 hours):", service_item.calculate_total(4))