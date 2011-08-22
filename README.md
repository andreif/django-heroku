# Initial Django site setup to run on Heroku (work in progress)

## 1. Installing prerequisites (Mac OS X)

### 1.1. [Pythonbrew](https://github.com/utahta/pythonbrew)

    curl -kL http://xrl.us/pythonbrewinstall | bash
    alias pyb='pythonbrew'

### 1.2. Python, [pip](http://pypi.python.org/pypi/pip), and setuptools

    pyb install --force 2.7.2
    pyb use 2.7.2

### 1.3. Setup a virtual environment

    deactivate
    rm ~/.pythonbrew/venvs/Python-2.7.2/heroku
    pyb venv create heroku --no-site-packages
    pyb venv use heroku

### 1.4. [RVM](http://beginrescueend.com/rvm/install/)

    bash < <(curl -s https://rvm.beginrescueend.com/install/rvm)
    rvm get latest

### 1.5. Ruby and [TextMate settings](http://beginrescueend.com/integration/textmate/)

    rvm install 1.9.2-p290
    rvm --default use 1.9.2-p290
    rvm @textmate --create
    rvm wrapper default@textmate textmate
    
In TextMate preferences
    
    TM_RUBY=/Users/andrei/.rvm/bin/textmate_ruby

### 1.6. [Homebrew](https://github.com/mxcl/homebrew/wiki/installation)

    ruby -e "$(curl -fsSL https://raw.github.com/gist/323731)"

### 1.7. [Node.js](github.com/joyent/node/wiki/Installation)

    brew install node

### 1.8. [npm](github.com/isaacs/npm)

    curl http://npmjs.org/install.sh | clean=yes sh




## 2. Creating a Django site

### 2.1. Install Django

    pip install Django

### 2.2. Create a fresh Django site

    mkdir ~/django-heroku
    cd ~/django-heroku
    django-admin.py startproject mysite
    cd mysite
    python manage.py runserver

### 2.3. Add a core app to the site

    python manage.py startapp core

# To do:

### Create a home page



## 3. Installing Django modules


### https://github.com/jezdez/django_compressor

### [Sass](http://sass-lang.com/download.html)

    gem install sass

### [Less](http://lesscss.org/)

    npm install less

### [coffee](github.com/jashkenas/coffee-script)

    brew install coffee-script

### https://github.com/zacharyvoase/cssmin

### http://code.google.com/closure/

