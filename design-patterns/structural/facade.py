class Inventory:
    def check_item(self):
        print("Checking of item A in stock")
        return True
        
class PaymentGateway:
    def process_payment(self):
        print("Processing payment for amount 300")
        return True
    
class ShippingService:
    def ship_item(self):
        print("Shipping item to address")
        return True
    
class OrderFacade:
    def __init__(self):
        self.inventory = Inventory()
        self.pg = PaymentGateway()
        self.shipping_service = ShippingService()
        
    def place_order(self):
        if self.inventory.check_item():
            if self.pg.process_payment():
                if self.shipping_service.ship_item():
                    return "Order Placed"
                return "Shipping Failed"
            return "Payment Failed"
        return "No Item found"
    
# Facade Pattern is where we provide a facade class with a simple interface  to the client 
# such that we hide all the internal complex implementation
if __name__ == "__main__":
    order =  OrderFacade()
    print(order.place_order())