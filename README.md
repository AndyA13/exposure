exposure
========

A website for hosting photos using S3.

Setup
=====

1. Install Postgres
2. mkvirtualenv exposure && pip install -r requiremens.txt
2. Copy exposure/settings_local.py.example to exposure/settings_local.py and customise.
3. ./manage.py syncdb
4. ./manage.py migrate
5. ./manage.py runserver


Configuration
=============

The following environment variables must be set for S3 support.

 - AWS_ACCESS_KEY_ID
 - AWS_SECRET_ACCESS_KEY
 - AWS_STORAGE_BUCKET_NAME

There is one other environment variable that can be set, SENTRY_DSN to
add support for getsentry.com.