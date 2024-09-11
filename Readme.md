## CapSync

>  **Description** : Capsync is a Api based  Backend program which helps the user to extract subtitles from a vedio and save in a DB (PostGres)

---

## SetUp Project 

> 1. Git Clone = git clone https://github.com/Prashant-Bhatt-2000/CapSync.git

> 2. Install requirements = pip install -r requirements.txt

> 3. Setup Postgres = (I have setup my own local postgres. SO Please setup accordingly or just use default sqlite one)
y

### Please Uncomment the Postgres Database in settings.py and comment sqlite Db if you want to poceed with Postgres. I have created setup for both.

### Postgres Local setup creds: 
```
    DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'CapSync',
         'USER': 'postgres',
         'PASSWORD': 'postgres',
         'HOST': 'localhost',
         'PORT': '5432',
     }
 }

```

## Setup Your own Gmail App password (necessary for email verification) 

```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'Please Use your own Email Id'
EMAIL_HOST_PASSWORD = 'Please Generate your own app password from Gmail App Password'
```
---
### Password Generation Steps

    ```
        1. Go to Manage accounts (Gmail)

        2. Setup 2 step verification

        3. Go to App Password. And Create one for testing this application.
    ```

---

## APIs

### Auth API's

    > Signup API : http://localhost:8000/api/accounts/signup/

    Data : {
            "username": "Prashant", 
            "email": "bhatt.prashant2000@gmail.com", 
            "password": "Password"
            } 

---
    > Signin API : http://localhost:8000/api/accounts/signin/

    Data : {
            "email": "bhatt.prashant2000@gmail.com", 
            "password": "Password"
           }


---

### Vedio Process APIS
#### (Note : These Apis need JWT tokens so Please Login and paste token in headers with Authorization field)

    > Upload Vedio API = http://localhost:8000/api/vedio/vedioupload

    Data in Form = title = "name of vedio"
                   video_file = path of vedio
                   video_thumbnail = path of any thumbnail you want.

---

    > Get Subtitle API = http://localhost:8000/api/vedio/getsubtitles/<video_id>


---
