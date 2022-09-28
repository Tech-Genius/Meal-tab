# Meal-tab
An ecommerce web app for showcasing a food restaurant, ordering food from the restaurant, and booking table appointments in the restaurant. Users can also fill the event reservation form to reserve their chefs for events. 

Technologies Used: Django, Bootstrap, Jquery, Sqlite, Css, Html, Ajax.

Live site available at http://meal-tab.herokuapp.com/ 

To run on your local machine:

Git Fork https://github.com/Tech-Genius/Meal-tab/

Make sure python is installed on your machine

cd into the forked folder

run "python -m venv my_virt_env " to create a virtual environment

run "pip install -r requirements.txt" to install all the dependencies

run "python manage.py makemigrations" to collect latest changes in the models.py

run "python manage.py migrate" to migrate to the latest changes in the models.py. NB: this will create a db.sqlite3 file if you don't have it already.

run "python manage.py loaddata data.json" to populate the database with some data

run "python manage.py runserver" to start the default local server

visit "localhost:8000" or copy the url printed out on your cli to visit the web app 

