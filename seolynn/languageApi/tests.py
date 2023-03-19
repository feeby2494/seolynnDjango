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
from django.forms.models import model_to_dict

from .models import Collection, Language, Word
from .views import WordListOrCreate, WordSingle, LanguageListOrCreate, LanguageSingle, CollectionListOrCreate

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

        # Made function for this part since I had to do this again after deleting it

        # I have no clue why this function deos not work to POST
        def test_endpoint(self, method, url, view, primary_key, data):
            if data:
                request = method(url, data=json.dumps(data), content_type='application/json', follow=True)
            request = method(url, follow=True)
            force_authenticate(request, user=self.admin_user)
            if primary_key:
                return view(request, pk=primary_key)
            return view(request)

        """
            Creating a Word using Post request under the Korean Language (id=1)
        """

        viewListOrCreate = WordListOrCreate.as_view()
        payload = {'name': '말', 'language': 1, 'collection' : None}
        # Make an authenticated request to the view...  
        create_one_request = self.factory.post('/api/v1/study/language/korean/words', data=json.dumps(payload), content_type='application/json', follow=True)
        force_authenticate(create_one_request, user=self.admin_user)
        create_one_response = viewListOrCreate(create_one_request)

        print(create_one_response)

        # What the fuck is going on
        # post_method=self.factory.post
        # post_url='/api/v1/study/language/1/word/'
        # post_view=viewListOrCreate
        # payload = {'name': '말', 'user':self.admin_user.id, 'language': 1}
        # create_one_response = test_endpoint(self, method=self.factory.post, url='/api/v1/study/language/1/word/', view=WordListOrCreate.as_view(), primary_key=None, data={'name': '말', 'user':self.admin_user.id, 'language': 1})
        # print(create_one_response.data)
        """
            Seeing if my word is created by using Get request
        """

        viewSingle = WordSingle.as_view()

        # get_single_response = test_get_one(self, view=viewSingle, primary_key=create_one_response.data['id'])
        method=self.factory.get
        url=f"/api/v1/study/language/korean/words/{create_one_response.data['id']}/"
        primary_key=create_one_response.data['id']
        view=viewSingle
        get_single_response = test_endpoint(self, method=method, url=url , view=view, primary_key=primary_key, data=None)

        self.assertEqual({'id' : create_one_response.data['id'], 'name': '말', 'language' : create_one_response.data['language'], 'collection': None}, get_single_response.data)

        """
            Deleting my word and seeing if my status code is 404 when doing the same Get request
        """
        
        method=self.factory.delete
        url=f"/api/v1/study/language/korean/words/{create_one_response.data['id']}/"
        primary_key=create_one_response.data['id']
        view=viewSingle
        delete_single_response = test_endpoint(self, method=method, url=url , view=view, primary_key=primary_key, data=None)

        method=self.factory.get
        url=f"/api/v1/study/language/korean/words/{create_one_response.data['id']}/"
        primary_key=create_one_response.data['id']
        view=viewSingle
        get_single_response = test_endpoint(self, method=method, url=url , view=view, primary_key=primary_key, data=None)
        
        self.assertEqual( get_single_response.status_code, 404)


    

    def test_create_language(self):

        self.client.force_login(user=self.admin_user)

        """
            Creating a Language using Post request
        """

        viewListOrCreate = LanguageListOrCreate.as_view()

        payload = {'name': 'Korean', 'user':self.admin_user.id}

        # Make an authenticated request to the view...  
        create_language_request = self.factory.post('/api/v1/study/language', data=json.dumps(payload), content_type='application/json', follow=True)
        force_authenticate(create_language_request, user=self.admin_user)
        create_language_response = viewListOrCreate(create_language_request)

        """
            Seeing if this created Language is in db by doing a get request for it by its primary key
        """
        viewSingleLanguage = LanguageSingle.as_view()

        get_single_language_request = self.factory.get(f"/api/v1/study/language/{create_language_response.data['slug']}/", follow=True)
        force_authenticate(get_single_language_request, user=self.admin_user)
        get_single_language_response = viewSingleLanguage(get_single_language_request, slug=create_language_response.data['slug'])

        self.assertEqual({'id' : create_language_response.data['id'],'name': 'Korean','slug' : 'korean' , 'user': create_language_response.data['user']}, get_single_language_response.data)
        # I'm not convenced in Test Driven Development, I could have wrote two apps in the time this took, and my test still deosn't save anything to the database

    def test_patch_put_word(self):

        """
            Patching latest word to have name of 'Dog'
        """

        viewPatchPutWord = WordSingle.as_view()
        payload = {'name': 'Dog'}

        latest_word = model_to_dict(Word.objects.latest('id'))

        print(latest_word)

        patch_latest_request = self.factory.patch(f"/api/v1/study/language/korean/words/{latest_word['id']}", data=json.dumps(payload), content_type='application/json', follow=True)
        force_authenticate(patch_latest_request, user=self.admin_user)
        create_language_response = viewPatchPutWord(patch_latest_request, pk=latest_word['id'])

        self.assertEqual(create_language_response.status_code, 200)

        """
            Doing Get request with latest word's id as the primary key to check if its name is 'Dog'
        """

        viewSinglePatchWord = WordSingle.as_view()

        get_single_Patch_Word_request = self.factory.get(f"/api/v1/study/language/korean/words/{latest_word['id']}/", follow=True)
        force_authenticate(get_single_Patch_Word_request, user=self.admin_user)
        get_single_language_response = viewSinglePatchWord(get_single_Patch_Word_request, pk=latest_word['id'])

        self.assertEqual({'id' : latest_word['id'],'name': 'Dog', 'language' : latest_word['language'], 'collection' : latest_word['collection']}, get_single_language_response.data)

    # def test_word_filter(self):

    #     # Make collection and words
    #     lang = Language.objects.filter(slug='korean')
    #     viewCreateCollection = CollectionListOrCreate.as_view()
    #     payload={'name' : 'first', 'slug' : 'first', 'language' : lang['id']}
    #     create_collection_request = self.factory.post('/api/v1/study/language/korean/collections', data=json.dumps(payload), content_type='application/json', follow=True)
    #     force_authenticate(create_collection_request, user=self.admin_user)
    #     create_language_response = viewCreateCollection(create_collection_request)


    #     # Make two word in new collection 'first'
    #     coll = Collection.objects.filter(slug='first')
    #     viewCreateWords = Word.as_view()
    #     payload=[{'name': '말1', 'language' : lang['id'], 'collection' : coll['id']}, {'name': '말2', 'language' : lang['id'] , 'collection' : coll['id']}]
    #     create_words_request = self.factory.post('/api/v1/study/language/korean/words/', data=json.dumps(payload), content_type='application/json', follow=True)
    #     force_authenticate(create_words_request, user=self.admin_user)
    #     create_language_response = viewCreateWords(create_words_request)


    #     viewFilteredWords = Word.as_view()

    #     get_filter_Word_request = self.factory.get(f"/api/v1/study/language/korean/words/?collection=first", follow=True)
    #     force_authenticate(get_filter_Word_request, user=self.admin_user)
    #     get_filter_Word_response = viewFilteredWords(get_filter_Word_request)

    #     self.assertEqual([{'name': '말1', 'language' : lang['id'], 'collection' : coll['id']}, {'name': '말2', 'language' : lang['id'] , 'collection' : coll['id']}], get_filter_Word_response.data)


   
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