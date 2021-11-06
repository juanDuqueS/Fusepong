# Fusepong

Fusepong is a project made in django;
Webpage: [Fusepong](http://jduques.pythonanywhere.com)
## Installation
Download the project
```bash
git clone https://github.com/juanDuqueS/Fusepong
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install venv in the root folder and activate it.

```bash
pip3 install virtualenv
```
Install the requirements
```bash
pip install -r requirements.txt
```
Migrate all the databases
```bash
python manage.py migrate
```
Load database 
```bash
python manage.py loaddata data.json
```
Run the app
```bash
python manage.py runserver
```
# ToDo
* add messages to notificate different status (ex: user created, ticket added succesfully, etc)
* Finish crud for companies, projects and histories
* After registering, redirect to homepage with the new user session