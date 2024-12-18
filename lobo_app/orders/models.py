from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    key = models.CharField(max_length=20, default="")

    class Meta:
        ordering = ["-created"]
        indexes = [models.Index(fields=["-created", "-email"])]

    def __str__(self):
        return f"Order {self.id}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    class Meta:
        ordering = ["-order"]
        indexes = [models.Index(fields=["-order"])]

    user = models.ForeignKey(
        User,
        related_name="bought_courses",
        on_delete=models.CASCADE,
        default=0,
    )
    order = models.ForeignKey(
        Order,
        related_name="items",
        on_delete=models.CASCADE,
    )
    course = models.ForeignKey(
        "cursos.Curso",
        related_name="order_items",
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
