#!/bin/bash
source /home/admin/envs/careerhelper/bin/activate
authbind gunicorn --bind 0.0.0.0:80 careerhelper.wsgi:application
