class PurchaseOrder:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items  # List of PurchaseOrderItem

class PurchaseOrderItem:
    def __init__(self, item_id, quantity, price):
        self.item_id = item_id
        self.quantity = quantity
        self.price = price
        self.total_price = self.quantity * self.price
