from fabric.api import *

env.hosts = ['www-01.abtech.org']
env.key_filename = ['~/.ssh/id_rsa_abtech']
env.user = 'deploy'


def pull():
    with cd('/srv/abtech.org'):
        run("git pull")

def touch():
    with cd('/srv/abtech.org'):
        run("touch abtech/wsgi.py")
