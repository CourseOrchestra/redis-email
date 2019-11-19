import os

from dotenv import load_dotenv

load_dotenv()
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/1')
QUEUES = ['email']

MAIL_SERVER = os.getenv('MAIL_SERVER')
if not MAIL_SERVER:
    raise EnvironmentError('MAIL_SERVER variable not defined')
MAIL_PORT = int(os.getenv('MAIL_PORT'))
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'False').lower() == 'true'
MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', 'True').lower() == 'true'

DEFAULT_TIMEOUT = int(os.getenv('DEFAULT_TIMEOUT', 10))
NAME = 'email-worker'
