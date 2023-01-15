# -*- coding: utf-8 -*-

import os
import sys
import platform

#путь к проекту
sys.path.insert(0, '/home/c/cs97511/robo/public_html/school_section')

#путь к фреймворку
sys.path.insert(0, '/home/c/cs97511/robo/public_html/school_section/school_section')

#путь к виртуальному окружению
sys.path.insert(0, '/home/c/cs97511/robo/venv/lib/python{0}/site-packages'.format(platform.python_version()[0:3]))
sys.path.insert(0, '/home/c/cs97511/robo/venv/lib/python3.6/site-packages')

os.environ["DJANGO_SETTINGS_MODULE"] = "school_section.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
