from django.db import models

class Broker(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    starting_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class Holding(models.Model):
    ticker = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    shares = models.DecimalField(max_digits=15, decimal_places=3)
    averagePPS = models.DecimalField(max_digits=10, decimal_places=2)
    totalCostBasis = models.DecimalField(max_digits=15, decimal_places=2)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)

    def __str__(self):
        return self.ticker

class Transaction(models.Model):
    buy = models.BooleanField()
    date = models.DateField()
    ticker = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    shares = models.DecimalField(max_digits=15, decimal_places=3)
    pricePerShare = models.DecimalField(max_digits=10, decimal_places=2)
    costBasis = models.DecimalField(max_digits=15, decimal_places=2)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    note = models.CharField(max_length = 100)

    def __str__(self):
        if (self.buy):
            return f'Bought {self.shares} shares of {self.symbol} on {self.date}'
        else:
            return f'Sold {self.shares} shares of {self.symbol} on {self.date}'