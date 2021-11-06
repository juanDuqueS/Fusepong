# Fusepong

# Activate the virtual enviroment
source venv/bin/activate

# Download the requirements
pip install -r requirements.txt

# To load data
python manage.py loaddata data.json

# ToDo
* add messages to notificate different status (ex: user created, ticket added succesfully, etc)
* Finish crud for companies, projects and histories