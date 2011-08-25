### Create a home page



## 3. Installing Django modules


### https://github.com/jezdez/django_compressor

### [Sass](http://sass-lang.com/download.html)

    gem install sass

### [Less](http://lesscss.org/)

    npm install less

### [CoffeeScript](github.com/jashkenas/coffee-script)

    brew install coffee-script

### https://github.com/zacharyvoase/cssmin

### http://code.google.com/closure/


### 2.5. Add a simple page
    
 - Create templates for layout and page
 - Add a view function
 
### 2.6. [HamlPy](https://github.com/jessemiller/HamlPy) templates

    pip install hamlpy
    pip install djaml

Add [template loader](https://github.com/chartjes/djaml).

Then create templates/index.haml



## 3. Installing SASS and CoffeeScript

### 3.1. [Sass](http://sass-lang.com/download.html) and [Compass](https://github.com/chriseppstein/compass)

    gem install sass
    gem install compass
    mkdir ~/django-heroku/mysite/media
    cd ~/django-heroku/mysite/media
    compass create compass [--using blueprint]
    cd compass
    compass watch

### 3.2. [Less](http://lesscss.org/)

    npm install -g less

### 3.3. [CoffeeScript](github.com/jashkenas/coffee-script)

    npm install -g coffee-script

### 3.4. [django_compressor](https://github.com/jezdez/django_compressor)

    pip install django-compressor

In order to work with HamlPy

    pip install BeautifulSoup

Add settings
http://django_compressor.readthedocs.org/en/latest/installation/
http://django_compressor.readthedocs.org/en/latest/settings/#compress-precompilers





http://www.pip-installer.org/en/latest/requirement-format.html

Pip currently supports cloning over git, git+http and git+ssh:

-e git://git.myproject.org/MyProject.git#egg=MyProject
-e git+http://git.myproject.org/MyProject/#egg=MyProject
-e git+ssh://git@myproject.org/MyProject/#egg=MyProject
Passing branch names, a commit hash or a tag name is also possible:

-e git://git.myproject.org/MyProject.git@master#egg=MyProject
-e git://git.myproject.org/MyProject.git@v1.0#egg=MyProject
-e git://git.myproject.org/MyProject.git@da39a3ee5e6b4b0d3255bfef95601890afd80709#egg=MyProject
