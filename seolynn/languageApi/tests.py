from urllib import request, response
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
# from rest_framework.test import APIClient
from django.test import Client
from django.test import TestCase
from django.urls import reverse
import unittest
import json
import requests
from .views import WordListOrCreate, WordSingle

from rest_framework.authtoken.models import Token


# Want to test frist baby steps to lanauge API


class TestLanguageApi(unittest.TestCase):

    def setUp(self):
        # store the password to login later
        password = 'mypassword' 

        self.admin_user, created = User.objects.get_or_create(username='test_admin', email='test_admin@test.com')
        if created:
            self.admin_user.set_password(password)
            self.admin_user.save()

        # self.admin_user.save()
        self.client = Client()

   
        

        


        

        self.client.force_login(user=self.admin_user)

        # You'll need to log him in before you can send requests through the client
        self.client.login(username=self.admin_user.username, password='mypassword')

        # token = Token.objects.get(user__username='test_admin')
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        
        self.factory = APIRequestFactory()

        
        

    def test_word_post_list(self):
        
        self.client.force_login(user=self.admin_user)

        viewListOrCreate = WordListOrCreate.as_view()

        payload = {'name': '말', 'user':self.admin_user.id}

        # Make an authenticated request to the view...  
        create_one_request = self.factory.post('/language/word', data=json.dumps(payload), content_type='application/json', follow=True)
        force_authenticate(create_one_request, user=self.admin_user)
        create_one_response = viewListOrCreate(create_one_request)

        viewSingle = WordSingle.as_view()

        get_single_request = self.factory.get(f"/language/word/{create_one_response.data['user']}/", follow=True)
        force_authenticate(get_single_request, user=self.admin_user)
        get_single_response = viewSingle(get_single_request, pk=create_one_response.data['user'])

        
        # headers = {'Content-type': 'application/json'}
        # request = self.client.post('/language/word', data=json.dumps(payload), content_type='application/json', follow=True)
        # # user=UserInstance, token=UserInstanceToke
        
        # response = requests.get('http://localhost:8000/language/word')

        print('JSON Output: \n', dir(create_one_response.data))
        print('JSON Output: \n', create_one_response.data['user'])

        self.assertEqual({'name': '말', 'user': create_one_response.data['user']}, get_single_response.data)



        # I'm not convenced in Test Driven Development, I could have wrote two apps in the time this took, and my test still deosn't save anything to the database




#  def test_admin_requests(self):
        # self.client.force_login(self.current_user)
        # self.assertEqual(int(self.client.session["_auth_user_id"]), self.current_user.pk)
        
        # data = {
        #         "project_list-TOTAL_FORMS": "2", 
        #         "project_list-INITIAL_FORMS" : "0", 
        #         "project_list-MIN_NUM_FORMS" : "0", 
        #         "project_list-MAX_NUM_FORMS" : "1000", 
        #         "project_list-0-hourly_contract" : "on", 
        #         "project_list-0-project_name" : "test-project-1", 
        #         "project_list-0-description" : "test-desc-1", 
        #         "project_list-1-hourly_contract" : "on", 
        #         "project_list-1-project_name" : "test-project-2", 
        #         "project_list-1-description" : "test-desc-2"}

        # response = self.client.post("/webservices/submit_multi_project/", data=data)

        # actual_order = WorkOrder.objects.latest('id')
        # actual_projects = Project.objects.filter(order= actual_order).all()

        # # self.assertEqual(response.status_code, 200 || 302)
        # self.assertEqual(model_to_dict(actual_projects[0])['project_name'], 'test-project-1')
        # self.assertEqual(model_to_dict(actual_projects[0])['description'], 'test-desc-1')
        # self.assertEqual(model_to_dict(actual_projects[1])['project_name'], 'test-project-2')
        # self.assertEqual(model_to_dict(actual_projects[1])['description'], 'test-desc-2')

        # # Clean up DB
        # Project.objects.filter(id=model_to_dict(actual_projects[0])['id']).delete()
        # Project.objects.filter(id=model_to_dict(actual_projects[0])['id']).delete() # Still at index zero, since we deleted first one
        # WorkOrder.objects.filter(id=model_to_dict(actual_order)['id']).delete()