import os


DATABASES = {
    'USER':'ROOT',
    'PASSWORD':'123456',
    'HOST':'127.0.0.1',
    'PORT':'3306',
    'DB':'ihome',
    'DIALECT':'mysql',
    'DRIVER':'pymysql'
}

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

UPLOAD_DIR = os.path.join(os.path.join(BASE_DIR,'static'),'upload')