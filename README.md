# my-app
## Project setup 

``` pip install djangorestframework ``` 


### Compiles and hot-reloads for development 


``` 1) first change your database settings according to your convinient way in settings.py ``` 

``` 2) intialize your database in your db client and make sure which database you are using for sqllite no need to install for my sql pip install mysqlclient```

``` 3) after according to your system you setup your database and initialize just use python manage.py makemigrations && migrate```

``` 4) to run in live server use python manage.py runserver make sure also notice pc condition also ```

``` 5) As told before after checking your pc condition if your pc condition is good to go then install Postman otherwise Thunder Client```

``` 6) now you can paste your localhost link in your Postman```


### Update , Read , View And Delete

```  1) User Registration: POST http://127.0.0.1:8000/api/register/ you cannot register a user while login so you have to logout first ``` 

``` 2) User Login: POST http://127.0.0.1:8000/api/login/  make sure you will get two token one is for access anything like to see role and create company and also joblisting of that company and also delete similarly for jobapplications also make sure to keep that token and also session will automatically expire in 10 minutes```

``` 3) User Role: GET http://127.0.0.1:8000/api/role/ in order to see role you must have to paste your access token in Header  field should be Authorriztion and value will be Bearer<access_token> similarly for joblisting and jobapplications also```

``` 4) Job Listings: GET/POST/PATCH/DELETE http://127.0.0.1:8000/api/joblistings/ ```

``` 4.1) for updating  Job listings : Patch http://127.0.0.1:8000/api/joblistings/id  and also for deleting DELETE http://127.0.0.1:8000/api/joblistings/id ```

``` 5) Job Applications: GET/POST/PATCH/DELETE http://127.0.0.1:8000/api/jobapplications/ ```

``` 6) for updating Job Applications : Patch http://127.0.0.1:8000/api/jobapplications/id and also for deleting DELETE http://127.0.0.1:8000/api/jobapplications/id ```

``` 7) for logout user: Post http://127.0.0.1:8000/api/logout/ and also take access token and put as I mentioned with these you also have to put {"refresh_token":"refresh_token"} in your body json format ```

``` 8) while login don't use hash password instead of that use created password that you have registered a user before ```

### Lints and fixes files 


``` python manage.py flush ``` 


### Customize configuration See [Configuration Reference](https://docs.djangoproject.com/en/5.1/topics/auth/customizing/). 

# SimpleDjangoRestAPI 

# SimpleProject 

# SimpleJOBAgencies 

# Reference

``` for simple reference go to the file name called Crud_Restapi.zip here is the manual guide how to fix some related issues ``` 

# HappyLife
