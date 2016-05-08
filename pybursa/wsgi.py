import os, sys
path = '/opt/myenv/ooniversity_django_courses_04'
#if path not in sys.path:
sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pybursa.settings")


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
