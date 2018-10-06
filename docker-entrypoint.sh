#!/bin/bash

set -eu

if [ "$1" = 'runproduction' ]; then
	exec python /a9d9969521233042c69706c5695c1f23/manage.py collectstatic --noinput && gunicorn app.wsgi -d 0.0.0.0:8000
elif [ "$1" = 'runserver' ]; then
	exec python /a9d9969521233042c69706c5695c1f23/manage.py runserver 0.0.0.0:8000
elif [ "$1" = 'test' ]; then
	exec python /a9d9969521233042c69706c5695c1f23/manage.py test
fi

exec $@
