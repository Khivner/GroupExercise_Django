#!/bin/bash
git clone https://github.com/Khivner/GroupExercise_Django ~/staging.groupexercise.khivner.net/htdocs
virtualenv ~/staging.groupexercise.khivner.net/htdocs
source ~/staging.groupexercise.khivner.net/htdocs/bin/activate
pip3 install django 
pip3 install mysqlclient
pip3 install gunicorn

ln -s ~/staging.groupexercise.khivner.net/shared/SECRETKEY.py ~/staging.groupexercise.khivner.net/htdocs/mysite
~/staging.groupexercise.khivner.net/mysite/manage.py migrate


