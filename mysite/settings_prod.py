from .settings import *

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'simpledjango',
       'USER': 'david',
       'PASSWORD': 'david123',
       'HOST': 'localhost',
       'PORT': '',
   }
}
