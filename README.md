
# Carsansar

DescriptionDescriptionDescriptionDescriptionDescriptionDescriptionDescription 


## Setting Up App before running
#### setting up data base

This is using mysql db , you need to [install](https://dev.mysql.com/downloads/installer/) and [setup](https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database) mysql for django. 
after that let django know db you are using

Add this in settings.py
```py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",   # backend engine of django for mysql
        "NAME": "carsansar",                    # Your mysql database name
        "USER": "root",                         # your mysql username
        "PASSWORD": "carsansar",                # Your mysql password
        "HOST": "localhost",                    # host name (default)
        "PORT": "3306",                         # port number (default)
    }
}

```
## Setting Up Email things

It also sends mail to user for auth related things, so you need Add your email and password here in settings.py which it will be using to send mail

*you need to allow logging in to your mail account by less secures apps, allow that* [from here](https://support.google.com/accounts/answer/6010255?hl=en)
```py
EMAIL_HOST_USER = "youremail@gmail.com"     # your email
EMAIL_HOST_PASSWORD = "your password"       # your  password
```

## Add admin's personal email address only in settings.py
Django notifies admin when new consult is submitted
```py
    USER_MAIL = "admin@gmail.com"
```

## creating admin user for admin


## Run Project
Run all commands in same dir in terminal 


Clone the project

```bash
  git clone repourl
```

Go to the project directory

```bash
  cd carsansar
```
Install [python](https://www.python.org/downloads/) 

Creating virtual enviroment
```bash
    pip install virtualenv      #installing virtualenv module
    python -m venv .env         # creates virtualenv with name ".env"
    .env\Scripts\Activate.ps1   # Activate virtual env 
```
Install dependencies/ requirements

```bash
  pip install -r requirements.txt
```

Migrate the changes in databae

```bash
  python3 manage.py makemigrations
  python3 manage.py migrate          #migrates all the tables and fields etc to the db
```
Run the App

```bash
  python3 manage.py runserver
  # open the localhost url in browser
```

Creating Admin user
```bash
python manage.py createsuperuser
# prompt will ask your for details, fill that and done
```
Open http://127.0.0.1:8000/admin/ for visit admin panel of app, and login using admin's credentials 

