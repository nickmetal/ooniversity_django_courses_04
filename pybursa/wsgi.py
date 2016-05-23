import os, sys
path = os.path.abspath(os.path.curdir)
#if path not in sys.path:
sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pybursa.settings")


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
