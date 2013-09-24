git push heroku master -f;
heroku run "./manage.py collectstatic -c --noinput";
heroku run "./manage.py syncdb --noinput";
heroku run "./manage.py migrate";