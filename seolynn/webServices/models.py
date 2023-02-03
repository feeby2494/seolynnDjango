from django.db import models
from django.contrib.auth.models import User

# Was going to extend User, but I realized it's better to do a one-to-one
# customers will need to log in using their user. when they make their first order, they will be 
# tested for having a record in customer table, if none, then one will be made for them.
# class Customer(models.Model):
#     slug = models.SlugField()
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __init__(self, slug, user):
#         self.slug = slug
#         self.user = user

#     def get_absolute_url(self):
#         return f"/{self.user.get_username()}/"

# one-to-many with customer=> one ; order: many
class WorkOrder(models.Model):
    slug = models.SlugField(null=True, blank=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="work_orders")
    #customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="order_list")

    def __str__(self):
        return f"{self.slug}"

    def calculate_total_cost(self):
        pass

    def get_absolute_url(self):
        return f"/webservices/{self.user.get_username()}/{self.slug}/"

# one-to-many with order=> one ; project: many
class Project(models.Model):
    slug = models.SlugField(null=True, blank=True)
    python = models.BooleanField(default=False)
    r_language = models.BooleanField(default=False)
    excel = models.BooleanField(default=False)
    machine_learning = models.BooleanField(default=False)
    hourly_contract = models.BooleanField(default=True)
    django = models.BooleanField(default=False)
    react = models.BooleanField(default=False)
    project_name = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)

    order = models.ForeignKey(WorkOrder, on_delete=models.PROTECT, related_name="project_list")

    def __str__(self):
        return f"{self.slug} ( Order ID:{self.order.id} )"

    def calculate_due_date(self):
        pass

    def calculate_total_cost(self):
        pass

    def get_absolute_url(self):
        return f"/webservices/{self.order.user.get_username()}/{self.order.id}/{self.id}/"