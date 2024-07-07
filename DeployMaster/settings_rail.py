from DeployMaster.settings import *

from decouple import config

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['web-production-22a4e.up.railway.app/']