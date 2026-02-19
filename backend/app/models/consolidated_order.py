from django.db import models

class ConsolidatedOrder(models.Model):
    # Define fields for ConsolidatedOrder
    order_number = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_number


class ConsolidatedOrderItem(models.Model):
    # Define fields for ConsolidatedOrderItem
    order = models.ForeignKey(ConsolidatedOrder, related_name='items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantity} x {self.product_name}'