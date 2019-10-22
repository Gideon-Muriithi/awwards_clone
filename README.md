# Awwards App
This is an awward clone app developed with django with the aim of getting a better understanding of django framework.

# Description
This is a simple clone of awward site. The app allows user to create accounts and login to them with their credentials. The site also supports uploading of projects one has done and their live links. Logged in users are able to view projects posted by other users on the home page of site and click on the project's image to view more detaials of the project, rate the projects based on design, content and usability and also make a review on a the projects.

# Set Up and Installations
Prerequisites
Ubuntu Software Python3.6 Postgres python virtualenv

Clone the project repo by running <git clone https://github.com/Gideon-Muriithi/awwards_clone>.

Create virtual environment by running <python3.6 -m venv pip virtual> while in the dirctory of the cloned project. Activate the virtual environment by running <source virtual/bin/activate>.

Install all the dependencies necessarry for running the application using this command: pip install-r requirements.txt

Create a database: psql then create the databse using this command: CREATE DATABASE awwards

Run migrations using these respective commmands: python3.6 manage.py makemigrations images then: python3.6 manage.py migrate

Run the app using this command: python3.6 manage.py runserver on the terminal.You can then open the app on your browser

Create .env file and paste the following text and fill your details where appropriate

###### SECRET_KEY = '<Secret_key>'
###### DBNAME = 'awwards'
###### USER = ''
###### PASSWORD = ''
###### DEBUG = True
###### EMAIL_USE_TLS = True
###### EMAIL_HOST = 'smtp.gmail.com'
###### EMAIL_PORT = 587
###### EMAIL_HOST_USER = ''
###### EMAIL_HOST_PASSWORD = ''
###### Run initial Migration python3.6 manage.py makemigrations gram python3.6 manage.py migrate Run the app python3.6 manage.py runserver Open terminal on localhost:8000

# Known bugs
User is not able to view projects he/she has posted

# Technologies used
Python 3.6
HTML
Bootstrap 4
JavaScript
Heroku
Postgresql

# Support and contact details
For any comments, reviews or advice contact me on gideonapptests@gmail.com.

MIT License
Copyright (c) Gideon Muriithi