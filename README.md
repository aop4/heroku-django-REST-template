## Scope
I think Django is an amazingly powerful tool, and I'm glad you're considering using it for a REST API. This repo builds off of Heroku's heroku-django-starter-template (https://github.com/heroku/heroku-django-template), so it's geared toward deployment on Heroku--it will make it really easy.  
This repo can also be used as a starting point for a full website with database/backend capabilities, and I'd consider it a sort of "quick start" guide to setting up a Django backend.  
I assume no familiarity with Django, but this won't teach you everything you might want to do with it--it'll just get you through the hairy setup steps.  

## Sample code
I added in a sample model, URLs, and views, as detailed at the end of this readme. If you don't want to deal with them, you can remove the corresponding code from `models.py`, `serializers.py`, `urls.py`, and `views.py`. If you're not familiar with Django or the Django REST framework, I suspect it will be extremely helpful to work from those examples, however.


## Setup

`apt-get install python-pip # install pip`  

`pip install django`  

Run this command:  
`django-admin.py startproject --template=https://github.com/aop4/heroku-django-REST-template/archive/master.zip --name=Procfile rest_api`

`cd` into the folder it created (it will be a copy of the repo, minus the commit history)

(Optional steps to work in a virtual environment:)  
`pip install virtualenv`  
`virtualenv venv # create a virtual environment`  
`source venv/bin/activate # activate the virtual environment (do for every new terminal window)`  
(End of optional steps)  

`pip install -r requirements.txt # install requirements`  

`apt-get install sqlite3 #install SQLite3`  

An empty SQLite database file `db.sqlite3` is in the repo for your convenience. I started it with DB Browser for SQLite  (https://sqlitebrowser.org/), a useful tool for probing the database. 

#### Environment variables

You need to have a `SECRET_KEY` and a `DEBUG` environment variable, or you can replace the lines that search for them in `rest_api/settings.py`. These are used in `settings.py` to allow flexibility between the local and server environments and protect your secret key from exposure via GitHub, etc. If you deploy to Heroku, make sure to set the environment variables on the server (`DEBUG` absolutely must be false for production). A secret key is just a string of random characters; I'd look into how to generate a good one for security purposes, but for the time being you can simply make it "snargledragons" or something. Debug should be `True` on your local machine (and again, NOT on the production server).  

For now, you can add  
```
export SECRET_KEY=my_secret_key
export DEBUG=True
```  
to your `~/.bashrc` file (then restart the terminal) or, if you're using `virtualenv`, to the bottom of the `venv/bin/activate` script (and then reactivate the virtual environment). This is Unix-specific syntax.  

#### Managing models  

Run `python manage.py migrate`  
This will apply your models in `models.py` to the database. Once you run it, you should see a table in the database called `rest_api_student` since there's a model called Student (creative, I know) in `models.py` at the moment. After you make any changes to the models, run `python manage.py makemigrations rest_api` followed by `python manage.py migrate`. You should see the changes take effect in the database. Try splitting the `name` field of the `Student` class into two different fields, `last_name` and `first_name,` or changing the name of the model (`Student`) to something that you'd actually put in your database, like `City` or `ZooAnimal`.

#### Running the server  

`python manage.py runserver`

Open up your browser and point it to `localhost:8000`

#### /admin page

At `localhost:8000/admin`, you'll see an admin interface featuring all the models you register in `rest_api/admin.py`. From the admin page, you can easily add, remove, and modify data in the database. `python manage.py createsuperuser` lets you create a username and password so that you can log in.


## Test the REST API in your browser

The Django REST Framework comes with a really simple way to test your REST API on the fly: an interactive browser interface for all your views--even when they're just returning JSON data.
As stated above, this "template" also comes with some pre-built stuff. It allows you to interact with a database of students (if you did the above steps correctly) through PUT, POST, GET, and DELETE requests. Let's try it in the browser.
The request handlers themselves are in `views.py`.

#### 1. Add a student  
After completing the setup steps and running the server, point your browser to `localhost:8000/students`. Add a JSON object with a `name` field to the textbox (`{"name": "Spam Spammerson"}`) and click the POST button. You've just made a POST request without any code! Splendid. Add another student.
You can also do this with something like curl, or JavaScript, of course. See http://www.django-rest-framework.org/tutorial/1-serialization/#testing-our-first-attempt-at-a-web-api for more ways to test your API.

#### 2. View all students
Point your browser to `localhost:8000/students` again (i.e., refresh the page). You should see a list of all the students you added. GET requests are done automatically when you visit the URL.

#### 3. View a single student
Using the ids you can see in `/students` during the above step, you can view a single student. Go to `localhost:8000/students/1` (assuming 1 is a valid ID).

#### 4. Modify a student
Go to the URL you were using to view a student in (3). Enter a JSON object with a *new* `name` field into the text box and click PUT. If you refresh the page to make a GET request on the student, you'll see it has a new name.

#### 5. Delete a student
Now, while you're on that `localhost:8000/students/<id>` page, hit the big red DELETE button, and then go to `localhost:8000/students` again. The student should be absent from the list.

## Further reading
Check out the code in `views.py`, `models.py`, and `serializers.py` that's backing this whole thing.
Hopefully you've seen some of the cool features of the Django REST Framework and want to do more exploring and building. Take a gander through the files, feel free to gut them and add your own code, and check out the Django REST Framework's tutorial: http://www.django-rest-framework.org/tutorial/1-serialization/

