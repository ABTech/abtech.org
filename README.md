#AB Tech Website
The website for the Carnegie Mellon Activities Board Technical Committee

Django Captcha App from: https://github.com/2buntu/2buntu-blog

##Issues
We all have them.

##Development
###Prerequisites
- [Python 3.4](https://www.python.org/downloads/)

###Setup
Clone this repo into your workspace.
I strongly recommend using a virtual environment when developing this and any other Python project.
```
$ cd abtech.org
$ python3 -m venv .
$ source bin/activate
$ pip3 install -r requirements.txt
```

###Running
```
$ ./manage.py runserver
```

##Contribute
Just send a pull request!

###Production
On a clean install of Debian:

Install Vim
```
apt-get install vim
update-alternatives --config editor
#Uncomment syntax on in /etc/vim/vimrc
```

Install git
```
sudo apt-get install git
git config --global user.name "Sam Abtek"
git config --global user.email abtech@andrew.cmu.edu
git config --global color.ui auto
```

Add ssh-key
https://help.github.com/articles/generating-ssh-keys/

Get repo
```
git clone git@github.com:ABTech/abtech.org.git
```

Install Python3 and Pip3
```
sudo apt-get install python3
sudo apt-get install python3-pip
sudo pip-3.2 install -r requirements.txt
sudo pip-3.2 install pathlib # Not necessary with python 3.4
```

Run dev server to check work so far
```
./manage.py runserver 0.0.0.0:8000
```

Configure smtp server on port 25
```
:)
```

Enable Apache mod_wsgi
```
sudo apt-get install libapache2-mod-wsgi-py3
make wsgi.py executable
chmod u+x abtech/wsgi.py
```

Create abtech/settings/secret.py with the necessary secret keys that are in example_secret.py

Edit abtech/settings/production.py and add your host as a string to ALLOWED_HOSTS

Edit existing apache config or add site file based on django-example.conf
Site configuration will need to be enabled
```
cp django-example.conf /etc/apache2/sites-available/django.conf
sudo a2dissite default
sudo a2ensite django.conf
```

To reload code changes on the site live:
```
touch abtech/wsgi.py
```
