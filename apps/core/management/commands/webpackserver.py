import atexit
import os
import signal
import subprocess

from django.conf import settings
from django_extensions.management.commands.runserver_plus import (
    Command as StaticfilesRunserverCommand,
)


class Command(StaticfilesRunserverCommand):
    def inner_run(self, *args, **options):
        self.start_webpack()
        return super().inner_run(*args, **options)

    def start_webpack(self):
        self.stdout.write("--> Starting webpack")
        self.webpack_process = subprocess.Popen(
            ["cd {0} && npm run watch".format(settings.STATIC_ROOT)],
            shell=True,
            stdin=subprocess.PIPE,
            stdout=self.stdout,
            stderr=self.stderr,
        )

        self.stdout.write(
            "--> webpack process on pid {0}".format(self.webpack_process.pid)
        )

        def kill_webpack_process(pid):
            self.stdout.write("--> Closing webpack process")
            os.kill(pid, signal.SIGTERM)

        atexit.register(kill_webpack_process, self.webpack_process.pid)
