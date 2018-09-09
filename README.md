I think Django is an amazingly powerful tool, and I'm glad you're considering using it for a REST API. This repo builds off of Heroku's heroku-django-starter template, so it's geared toward deployment on Heroku--it will make it really easy.  
This repo can also be used as a starting point for a full website with database/backend capabilities, and I'd consider it a sort of "quick start" guide to setting up a Django backend.  

`cd` into this directory.

`apt-get install python-pip` # install pip  

(Optional steps to work in a virtual environment:)  
`pip install virtualenv`
`virtualenv venv`
`source venv/bin/activate`
(End of optional steps)  

`pip install -r requirements.txt`  

`apt-get install sqlite3`  

An SQLite database is in the repo for your convenience. I started it with DB Browser for SQLite 3 (https://sqlitebrowser.org/), a useful tool for probing the database. I don't know if you technically need sqlite3 installed, but I'm guessing you do.  

You need to have a `SECRET_KEY` and a `DEBUG` environment variable, or you can replace the lines that search for them in `rest_api/settings.py`. These are used in `settings.py` to allow flexibility between the local and server environments and protect your secret key from exposure via GitHub, etc. If you deploy to Heroku, make sure to set the environment variables on the server (`DEBUG` absolutely must be false for production). A secret key is just a string of random characters; I'd look into how to generate a good one for security purposes, but for the time being you can make it "snargledragons" or something. Debug can be `True` on your local machine.  

You can add  
```
export SECRET_KEY=my_secret_key
export DEBUG=True
```  
to your `~/.bashrc` file or, if you're using `virtualenv`, to the bottom of the `venv/bin/activate` script. This is Unix-specific syntax.

`python manage.py migrate` will apply the changes to your models in models.py to the database. Once you run it, you should see a table in the database called `rest_api_datamodel`. After you make any changes you make to the models, run `python manage.py makemigrations rest_api` followed by `python manage.py migrate`. You should see the changes take effect in the database. Try splitting the `name` field of DataModel into two different fields, `last_name` and `first_name,` or changing the name of the model (`DataModel`) to something that you'd actually put in your database, like `City`.

`python manage.py runserver`

Open up your browser and point it to `localhost:8000`

At `localhost:8000/admin`, you'll see an admin interface featuring all the models you register in `rest_api/admin.py`. From the admin page, you can easily add, remove, and modify data in the database. `python manage.py createsuperuser` lets you create a username and password for an admin account.

