# Initial Django site setup to run on Heroku (work in progress)


## 1. Installing prerequisites (Mac OS X)

See PREREQUISITES.md


## 2. Creating a Django site

### 2.1. Create a fresh Django site

    mkdir ~/django-heroku && cd $_
    django-admin.py startproject mysite
    cd mysite
    python manage.py runserver

### 2.2. Add a core app to the site

    python manage.py startapp core

### 2.3. Set up database and directories in the settings

 - Keep the root dir in a variable
 - Set sqlite3 as db driver and provide the path to db file
 - Set media root path
 - Set templates path

Sync the database

    python manage.py syncdb


