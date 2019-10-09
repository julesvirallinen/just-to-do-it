# TO-DO webapp

A simple to-do app with category filtering, deadlines, do after-dates and simple interface. Tasks are saved by user account.

This is a port of my excel to-do app. 

[Heroku](https://just-to-do-it.herokuapp.com/)
Test login: user/pass

## Documentation
* [Full relational diagram](/documentation/tietokantakaavio.png)
* [Current relational diagram](/documentation/tietokantakaavio2.png)
* [User stories](/documentation/user_stories.md)
* [Create tables](/documentation/create_tables.md)

### Installation 

You need to have 
* [Python 3.5 or higher](https://www.python.org/downloads/)
* [Pythons pip library](https://packaging.python.org/key_projects/#pip)
* [Virtual environment venv for python](https://docs.python.org/3/library/venv.html)
* [PostgreSQL](https://www.postgresql.org/)
* [pgAdmin for managing database](https://www.pgadmin.org/)


#### Setting up developement database server

In pgAdmin, create a local database server with
* Host name: localhost
* Port: 5432
* Username: postgres
* Password: newPassword

#### Download and start

1. Clone this repository and enter it's root
2. Create venv `python3 -m venv venv`
3. Start venv with `source venv/bin/activate`
4. Install dependencies `pip install -r requirements.txt`
5. Start server with `python run.py`

The app should now be running on localhost:5000

#### Deploying to Heroku 

This assumes you have `heroku-cli` installed and logged in. 

1. Create `procfile` for Heroku. `echo "web: gunicorn --preload --workers 1 application:app" > Procfile`
2. If you added any packages run `pip freeze | grep -v pkg-resources > requirements.txt` to inform Heroku of packages. 
3. Create Heroku app `heroku apps:create NAME` This will also create git remote
4. Add heroku to local git `git remote add heroku https://git.heroku.com/NAME.git`
5. Push to heroku with `git push heroku master`

### Usage

#### Accounts
You cannot do anything in the app without logging in. Create an account from the button in the top right corner. The browser will remember your login until you logout. 

#### Basic features

Add categories for tasks from "Add category". Delete categories from the category page. 

Add tasks by pressing "Add task". Delete or edit tasks by clicking on the task on the task list.
"Cannot be done before" indicates the first possible date to do a task. 

Press Category names on front page to filter tasks by category. If you add a task while filtering by category the task will have that category as default. 

When adding tasks, by adding a "Cannot be done before" -date the task will appear grayed out until it can be done. 

### Missing features
- Prerequisite-tasks - tasks that must be done before a task can be done. 