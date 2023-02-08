from django.test import TestCase
import subprocess

# Create your tests here.
#Login as admin

userName = 'jlynn'
userPassword = 'mj1268\"Samdasu'
requestBody = {}
requestUrl = f"http://localhost:8000/login"


loginCommand = f"curl -u '{userName}':'{userPassword}' -d '{requestBody}' -X POST {requestUrl}"
process = subprocess.Popen(loginCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

#Login as regular test user
