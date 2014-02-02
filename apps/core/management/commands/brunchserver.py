import os
import subprocess
import atexit
import signal

from django.conf import settings
from django.contrib.staticfiles.management.commands.runserver import Command\
    as StaticfilesRunserverCommand


class Command(StaticfilesRunserverCommand):

    def inner_run(self, *args, **options):
        self.start_brunch()
        return super().inner_run(*args, **options)

    def start_brunch(self):
        self.stdout.write('--> Starting brunch')
        self.brunch_process = subprocess.Popen(
            ['cd {0} && npm start'.format(settings.BRUNCH_DIR)],
            shell=True,
            stdin=subprocess.PIPE,
            stdout=self.stdout,
            stderr=self.stderr,
        )

        self.stdout.write('--> Brunch process on pid {0}'.format(self.brunch_process.pid))

        def kill_brunch_process(pid):
            self.stdout.write('--> Closing brunch process')
            os.kill(pid, signal.SIGTERM)

        atexit.register(kill_brunch_process, self.brunch_process.pid)
