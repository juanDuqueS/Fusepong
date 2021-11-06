# Fusepong

# Activate the virtual enviroment
source venv/bin/activate

# Download the requirements
pip install -r requirements.txt

# To load data
python manage.py loaddata data.json

# WebPage
* http://jduques.pythonanywhere.com

# ToDo
* add messages to notificate different status (ex: user created, ticket added succesfully, etc)
* Finish crud for companies, projects and histories
* After registering, redirect to homepage with the new user session