from django.db import models
from django.contrib.auth.models import User

# Was going to extend User, but I realized it's better to do a one-to-one
# customers will need to log in using their user. when they make their first order, they will be 
# tested for having a record in customer table, if none, then one will be made for them.
class Customer(models.Model):
    slug = models.SlugField()
    user = models.OneToOneField(User)

# one-to-many with customer=> one ; order: many
class Order(models.Model):
    slug = models.SlugField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="order_list")

    def calculate_total_cost(self):
        pass

# one-to-many with order=> one ; project: many
class Project():
    slug = models.SlugField()
    python = models.BooleanField(default=False)
    r_language = models.BooleanField(default=False)
    excel = models.BooleanField(default=False)
    machine_learning = models.BooleanField(default=False)
    hourly_contract = models.BooleanField(default=True)
    django = models.BooleanField(default=False)
    react = models.BooleanField(default=False)

    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="project_list")

    def calculate_due_date(self):
        pass

    def calculate_total_cost(self):
        pass

    def get_absolute_url(self):
        return f"/{self.order.customer.slug}/{self.order.slug}/{self.slug}/"