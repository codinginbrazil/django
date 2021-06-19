#!/usr/bin/env python
"""Django's command-line utility for administrative tasks.
    - A command-line utility that lets you interact with this Django project in various ways
    - Um utilitário de linha de comando 
        que permite a você interagir com esse projeto Django de várias maneiras
    - [docs](https://docs.djangoproject.com/en/3.2/ref/django-admin/)
"""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
