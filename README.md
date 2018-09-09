## Scope
I think Django is an amazingly powerful tool, and I'm glad you're considering using it for a REST API. This repo builds off of Heroku's heroku-django-starter-template (https://github.com/heroku/heroku-django-template), so it's geared toward deployment on Heroku--it will make it really easy.  
This repo can also be used as a starting point for a full website with database/backend capabilities, and I'd consider it a sort of "quick start" guide to setting up a Django backend.  
I assume no familiarity with Django, but this won't teach you everything you might want to do with it--it'll just get you through the hairy setup steps.


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
This will apply your models in `models.py` to the database. Once you run it, you should see a table in the database called `rest_api_datamodel` since there's a model called DataModel (creative, I know) in `models.py` at the moment. After you make any changes to the models, run `python manage.py makemigrations rest_api` followed by `python manage.py migrate`. You should see the changes take effect in the database. Try splitting the `name` field of the `DataModel` class into two different fields, `last_name` and `first_name,` or changing the name of the model (`DataModel`) to something that you'd actually put in your database, like `City` or `ZooAnimal`.

#### Running the server  

`python manage.py runserver`

Open up your browser and point it to `localhost:8000`

#### /admin page

At `localhost:8000/admin`, you'll see an admin interface featuring all the models you register in `rest_api/admin.py`. From the admin page, you can easily add, remove, and modify data in the database. `python manage.py createsuperuser` lets you create a username and password so that you can log in.

