# TO-DO webapp

A simple to-do web-app, where the user can set prerequisite tasks when adding tasks, as well as dates that the task cannot be done before. This way, the user can see everything they must do, but only see the tasks that they are able to do at any given moment. 

A task can be added to a category. Tasks are primarily on one page, but the user can filter tasks by one or more filters, or by deadline.

This is a port of my excel to-do app. 

[Heroku](https://just-to-do-it.herokuapp.com/)
Test login: user/pass

## Documentation
* [Relational diagram](/documentation/tietokantakaavio.png)
* [User stories](/documentation/user_stories.md)

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
