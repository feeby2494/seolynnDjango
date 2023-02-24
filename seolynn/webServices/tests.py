import subprocess
from urllib import response

# Create your tests here.
#Login as admin

# userName = 'jlynn'
# userPassword = 'mj1268\"Samdasu'
# requestBody = {}
# requestUrl = f"http://localhost:8000/login"


# loginCommand = f"curl -u '{userName}':'{userPassword}' -d '{requestBody}' -X POST {requestUrl}"
# process = subprocess.Popen(loginCommand.split(), stdout=subprocess.PIPE)
# output, error = process.communicate()

#Login as regular test user


from .models import WorkOrder, Project
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
import unittest

class WebServicesModelsTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

        test_user, created = User.objects.get_or_create(username='test_admin', password='mypassword')
        if created:
            test_user.save()

        self.current_login = self.client.post('/account/login/', {'username':'test_admin', 'password':'mypassword'})
        self.current_user = User.objects.get(username='test_admin')
        
    def test_admin_user_can_make_order_multiple_projects(self):
        
        
        new_order = WorkOrder.objects.create(user = self.current_user)
        new_order.slug = f"{self.current_user.get_username()}_order_{str(new_order.date_submitted).replace(' ', '_').replace(':', '_'). replace('+', '_').replace('.', '_').replace('-', '_')}"
        new_project1 = Project.objects.create(python=True, r_language=False, excel=False, machine_learning=True, hourly_contract=False, django=True, react=False, project_name='First App', description='My first app.', order= new_order)
        new_project2 = Project.objects.create(python=True, r_language=False, excel=False, machine_learning=True, hourly_contract=False, django=True, react=False, project_name='Second App', description='My second app.', order=new_order)

        new_order.save()
        new_project1.save()
        new_project2.save()

        test_order = {'id' : new_order.id, 'slug' : f"test_admin_order_{str(new_order.date_submitted).replace(' ', '_').replace(':', '_'). replace('+', '_').replace('.', '_').replace('-', '_')}", 'user' : 4}
        test_project1 = {'id' : new_project1.id, 'slug' : None, 'python' : True, 'r_language' : False, 'excel' : False, 'machine_learning' : True, 'hourly_contract' : False, 'django' : True, 'react' : False, 'project_name' : 'First App', 'description' : 'My first app.', 'order' : new_order.id}
        test_project2 = {'id' : new_project2.id, 'slug' : None, 'python' : True, 'r_language' : False, 'excel' : False, 'machine_learning' : True, 'hourly_contract' : False, 'django' : True, 'react' : False, 'project_name' : 'Second App', 'description' : 'My second app.', 'order' : new_order.id}

        


        self.assertEqual(test_order, model_to_dict(new_order))
        self.assertEqual(test_project1, model_to_dict(new_project1))
        self.assertEqual(test_project2, model_to_dict(new_project2))

        
        Project.objects.filter(id=new_project1.id).delete()
        Project.objects.filter(id=new_project2.id).delete()
        WorkOrder.objects.filter(id=new_order.id).delete()

    ## Think we need to take the slugs out, simplify the amount of vars

    def test_admin_requests(self):
        self.client.force_login(self.current_user)
        self.assertEqual(int(self.client.session["_auth_user_id"]), self.current_user.pk)
        
        data = {
                "project_list-TOTAL_FORMS": "2", 
                "project_list-INITIAL_FORMS" : "0", 
                "project_list-MIN_NUM_FORMS" : "0", 
                "project_list-MAX_NUM_FORMS" : "1000", 
                "project_list-0-hourly_contract" : "on", 
                "project_list-0-project_name" : "test-project-1", 
                "project_list-0-description" : "test-desc-1", 
                "project_list-1-hourly_contract" : "on", 
                "project_list-1-project_name" : "test-project-2", 
                "project_list-1-description" : "test-desc-2"}

        response = self.client.post("/webservices/submit_multi_project/", data=data)

        actual_order = WorkOrder.objects.latest('id')
        actual_projects = Project.objects.filter(order= actual_order).all()

        # self.assertEqual(response.status_code, 200 || 302)
        self.assertEqual(model_to_dict(actual_projects[0])['project_name'], 'test-project-1')
        self.assertEqual(model_to_dict(actual_projects[0])['description'], 'test-desc-1')
        self.assertEqual(model_to_dict(actual_projects[1])['project_name'], 'test-project-2')
        self.assertEqual(model_to_dict(actual_projects[1])['description'], 'test-desc-2')

        # Clean up DB
        Project.objects.filter(id=model_to_dict(actual_projects[0])['id']).delete()
        Project.objects.filter(id=model_to_dict(actual_projects[0])['id']).delete() # Still at index zero, since we deleted first one
        WorkOrder.objects.filter(id=model_to_dict(actual_order)['id']).delete()


# not saving anything to DB, so trying old curl: How to pass my crsf token?

        # loginCommand = f"curl -u 'jlynn:testOne' -d project_list-TOTAL_FORMS=2&project_list-INITIAL_FORMS=0&project_list-MIN_NUM_FORMS=0&project_list-MAX_NUM_FORMS=1000&project_list-0-hourly_contract=on&project_list-0-project_name=test-1&project_list-0-description=test-1&project_list-1-hourly_contract=on&project_list-1-project_name=test-2&project_list-1-description=test-2 -H application/x-www-form-urlencoded -X POST http://localhost:8000/webservices/submit_multi_project/"
        # process = subprocess.Popen(loginCommand.split(), stdout=subprocess.PIPE)
        # output, error = process.communicate()

        # response = self.client.post("/webservices/submit_multi_project/", data=data, content_type="application/x-www-form-urlencoded")



# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.webdriver import WebDriver

# class MySeleniumTests(StaticLiveServerTestCase):
#     fixtures = ['user-data.json']

#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.selenium = WebDriver()
#         cls.selenium.implicitly_wait(10)

#     @classmethod
#     def tearDownClass(cls):
#         cls.selenium.quit()
#         super().tearDownClass()

#     def test_login(self):
#         self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
#         username_input = self.selenium.find_element(By.NAME, "username")
#         username_input.send_keys('myuser')
#         password_input = self.selenium.find_element(By.NAME, "password")
#         password_input.send_keys('secret')
#         self.selenium.find_element(By.XPATH, '//input[@value="Log in"]').click()

## Think we need to take the slugs out, simplify the amount of vars


