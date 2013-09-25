#!/bin/sh

remote="$(git symbolic-ref HEAD 2>/dev/null)"

remote=${remote##refs/heads/}

if [ -n "$1" ]; then
    remote="$1";
fi

read -p "Press [Enter] key to deploy $remote to Heroku."

git push heroku $remote:master -f;
heroku run "./manage.py collectstatic --noinput";
heroku run "./manage.py syncdb --noinput";
heroku run "./manage.py migrate";
heroku ps:scale web=0 && heroku ps:scale web=1;