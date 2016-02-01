#!/usr/bin/env python
import coverage
import os
import sys

if __name__ == "__main__":

    try:
        test = sys.argv[1] == 'test'
    except IndexError:
        test = False

    if test:
        cov = coverage.coverage()
        cov.erase()
        cov.start()

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "djangosite.settings.default")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

    if test:
        cov.stop()
        cov.save()
        cov.report()
        cov.html_report()
