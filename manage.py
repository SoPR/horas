#!/usr/bin/env python
import os
import sys

import dotenv
dotenv.read_dotenv()

if __name__ == "__main__":
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'DEVELOPMENT').title()

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'horas.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', ENVIRONMENT)

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
