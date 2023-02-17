import subprocess

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

class WebServicesTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_admin_user_can_make_order_multiple_projects(self):
        User.objects.create(username='jlynn', password='testOne')
        current_login = self.client.post('/account/login/', {'username': 'jlynn', 'password': 'testOne'})
        current_user = User.objects.get(username='jlynn')
        new_order = WorkOrder.objects.create(user = current_user)
        new_order.slug = f"{current_user.get_username()}_order_{str(new_order.date_submitted).replace(' ', '_').replace(':', '_'). replace('+', '_').replace('.', '_').replace('-', '_')}"
        new_project1 = Project.objects.create(python=True, r_language=False, excel=False, machine_learning=True, hourly_contract=False, django=True, react=False, project_name='First App', description='My first app.', order= new_order)
        new_project2 = Project.objects.create(python=True, r_language=False, excel=False, machine_learning=True, hourly_contract=False, django=True, react=False, project_name='Second App', description='My second app.', order=new_order)

        test_order = {'id' : 1, 'slug' : f"jlynn_order_{str(new_order.date_submitted).replace(' ', '_').replace(':', '_'). replace('+', '_').replace('.', '_').replace('-', '_')}", 'user' : 1}
        test_project1 = {'id' : 1, 'slug' : None, 'python' : True, 'r_language' : False, 'excel' : False, 'machine_learning' : True, 'hourly_contract' : False, 'django' : True, 'react' : False, 'project_name' : 'First App', 'description' : 'My first app.', 'order' : 1}
        test_project2 = {'id' : 2, 'slug' : None, 'python' : True, 'r_language' : False, 'excel' : False, 'machine_learning' : True, 'hourly_contract' : False, 'django' : True, 'react' : False, 'project_name' : 'Second App', 'description' : 'My second app.', 'order' : 1}

        print(model_to_dict(new_project2))
        print(test_project2)


        self.assertEqual(test_order, model_to_dict(new_order))
        self.assertEqual(test_project1, model_to_dict(new_project1))
        self.assertEqual(test_project2, model_to_dict(new_project2))

## Think we need to take the slugs out, simplify the amount of vars