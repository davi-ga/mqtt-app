"""
This module contains a Django management command to start a Celery worker
with autoreload functionality. It defines a command that kills any running
Celery processes and starts a new Celery worker with the specified settings.
"""

import shlex
import subprocess

from django.core.management.base import BaseCommand
from django.utils import autoreload


def restart_celery():
    """
    Kills any running Celery processes and starts a new Celery worker
    with the specified settings.
    """
    cmd = "pkill celery"
    subprocess.call(shlex.split(cmd))
    cmd = "celery -A core.jobs.celery worker --beat --loglevel=info"
    subprocess.call(shlex.split(cmd))


class Command(BaseCommand):
    """
    Django management command to start a Celery worker with autoreload functionality.
    """

    def handle(self, *args, **options):
        print("Starting celery worker with autoreload...")
        autoreload.run_with_reloader(restart_celery)
