#AB Tech Website
The website for the Carnegie Mellon Activities Board Technical Committee

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
>git clone git@github.com:ABTech/abtech.org.git

Install Python3 and Pip3
```
sudo apt-get install python3
sudo apt-get install python3-pip
sudo pip-3.2 install -r requirements.txt
sudo pip-3.2 install pathlib # Not necessary with python 3.4
```

Run dev server to check work so far
> ./manage.py runserver 0.0.0.0:8000

Enable Apache mod_wsgi
>sudo apt-get install libapache2-mod-wsgi-py3
make wsgi.py executable
>chmod u+x abtech/wsgi.py

Add django apache config
```
cp django.conf /etc/apache2/sites-available/django.conf
sudo a2dissite default
sudo a2ensite django.conf
```

Export SECRET_KEY
>export SECRET_KEY=shhh it's a secret



