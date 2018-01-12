# Django Emergency Contact Wallpaper

This is a Django implimentation of my project called "emergency_contact_wallpaper"

### Requirments

certifi==2017.11.5

chardet==3.0.4

Django==1.11.8

idna==2.6

Pillow==5.0.0

pytz==2017.3

requests==2.18.4

urllib3==1.22

### virtualenv & project setup

1. Create new virtualenv with python version 3

		python -m virtualenv -p python 3 django-emergency-contact-wallpaper
    
		cd django-emergency-contact-wallpaper
    
		source bin/activate
    
2. Copy all the files/dirs of the repo to this dir

3. Install all the dependencies

		pip install -r requirements.txt
		
4. Create media folder
		
		mkdir media

5. Migrate the database

		python manage.py makemigrations && python manage.py migrate
    
6. Create superuser

		python manage.py createsuperuser
		
7. Run the server

		python manage.py runserver
