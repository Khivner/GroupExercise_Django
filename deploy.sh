#!/bin/bash

PROJECT_FOLDER=/home/khivner/staging.groupexercise.khivner.net/htdocs
SHARED_FOLDER=/home/khivner/staging.groupexercise.khivner.net/shared
GIT_URL=https://github.com/Khivner/GroupExercise_Django
CURRENT_BRANCH=master

# Clone if not exists
if [ ! -d "$PROJECT_FOLDER" ] ; then
	git clone "$GIT_URL" "PROJECT_FOLDER"
fi

# Update project to current branch
cd $PROJECT_FOLDER && git fetch --all 
cd $PROJECT_FOLDER && git checkout --force "origin/$CURRENT_BRANCH"

# symlink all relevant items
ln -sf $SHARED_FOLDER/SECRETKEY.py $PROJECT_FOLDER/mysite
ln -sf $SHARED_FOLDER/bin $PROJECT_FOLDER
ln -sf $SHARED_FOLDER/tmp $PROJECT_FOLDER

# install necessary packages

$PROJECT_FOLDER/bin/pip3 install django 
$PROJECT_FOLDER/bin/pip3 install mysqlclient
$PROJECT_FOLDER/bin/pip3 install gunicorn

# Run Migrations
$PROJECT_FOLDER/bin/python3 $PROJECT_FOLDER/manage.py migrate

sudo /sbin/reload khivner.groupexercise.staging

sudo /sbin/reload khivner.groupexercise.staging