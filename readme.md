## Welcome to Seolynn Django App!

#### Steps to get this going locally:

##### Step 1: Fork this repo

##### Step 2: Clone your forked repo

##### Step 3: Recomended to create a new branch => git branch <name_of_new_branch>

##### Step 4: You have a choice to use pip or pipenv: Recomend pipenv

##### Step 5: run: pipenv shell

##### Step 6: run: pipenv install

##### Step 7: Create .env file at /seolynn/seolynn/.env

##### Step 8: Enter your info into .env:

MYSQL_DATABASE_NAME='<name of your local mysql database>'
MYSQL_DATABASE_USERNAME='<username of your local mysql database>'
MYSQL_DATABASE_PASSWORD='<password of your local mysql database user>'
GMAIL_SMTP_USER='<email of the email you want to use to send emails to new site users>'
GMAIL_SMTP_PASSWORD='password of that email'
GMAIL_APP_PASSWORD="password for a gmail app, I recommend setting up a gmail app in your gmail settings" 
DJANGO_ALLOWED_HOSTS='*'
MYSQL_DATABASE_URI='localhost'
MYSQL_DATABASE_PORT='3306'
DEBUG='True'

##### If you want to use SQLite instead of mySQL:

MYSQL_DATABASE_NAME=
MYSQL_DATABASE_USERNAME=
MYSQL_DATABASE_PASSWORD=
GMAIL_SMTP_USER='<email of the email you want to use to send emails to new site users>'
GMAIL_SMTP_PASSWORD='password of that email'
GMAIL_APP_PASSWORD="password for a gmail app, I recommend setting up a gmail app in your gmail settings" 
DJANGO_ALLOWED_HOSTS='*'
MYSQL_DATABASE_URI=
MYSQL_DATABASE_PORT=
DEBUG='True'

Leave all MYSQL vars blank or delete them completly, a sqlite db will be created automatically if these are missing!

##### Step 10: Make sure you are in your virtual env and run: python manage.py migrate

##### Step 11: run: python manage.py collectstatic

##### Step 12: run: python manage.py createsuperuser

##### Step 13: run: python manage.py runserver

If your styles are not loading, then make sure DEBUG='True' in in your .env file!

