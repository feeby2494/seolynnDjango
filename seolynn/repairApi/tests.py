from .models import Repair, Order, Customer 
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.forms.models import model_to_dict

class RepairTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_admin_user_can_make_order_multiple_repairs(self):
        
        current_login = self.client.post('/account/login/', {'username': 'jlynn', 'password': 'testOne'})
        current_user = User.objects.get(username='jlynn')

        response = self.client.post("/repair/", {
            'project_list-TOTAL_FORMS': 2, 
            'project_list-INITIAL_FORMS' : 0, 
            'project_list-MIN_NUM_FORMS' : 0, 
            'project_list-MAX_NUM_FORMS' : 1000, 
            'project_list-0-hourly_contract' : 'on', 
            'project_list-0-project_name' : '1', 
            'project_list-0-description' : '1', 
            'project_list-1-hourly_contract' : 'on', 
            'project_list-1-project_name' : '2', 
            'project_list-1-description' : '2'}, content_type="application/x-www-form-urlencoded")


        actual_repair1 = Repair.objects.order_by('-id')[0]
        actual_repair2 = Repair.objects.order_by('-id')[1]

        self.assertEqual(model_to_dict(actual_repair1)['project_name'], '1')
        self.assertEqual(model_to_dict(actual_repair1)['description'], '1')
        self.assertEqual(model_to_dict(actual_repair1)['project_name'], '2')
        self.assertEqual(model_to_dict(actual_repair1)['description'], '2')

## Think we need to take the slugs out, simplify the amount of vars