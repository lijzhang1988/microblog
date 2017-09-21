import os
basedir = os.path.abspath(os.path.dirname(__file__))


CSRF_ENABLED = True
#
SECRET_KEY = 'you -will-never-guess'

#file upload path
UPLOAD_FOLDER = '/root/PycharmProjects/microblog/app/static/resources'

#mail server
MAIL_SERVER = 'smtp.qq.com'
#MAIL_SERVER = 'imap-mail.outlook.com'
MAIL_PORT = 465
#MAIL_PORT = 993
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = '2788099147@qq.com'
MAIL_PASSWORD = 'ehxderkunugodgcj'

#administrator list
ADMINS = ['2788099147@qq.com']


#log file
LOG_FILE = 'app/tmp/microblog.log'

#one page show list limit
POSTS_PER_PAGE = 3

#all file search
WHOOSH_BASE = os.path.join(basedir,'search.db')
MAX_SEARCH_RESULTS = 10


#more languages
LANGUAGES = {
    'en':'English',
    'zh':'中文'
}


BAIDU_APP_ID = '20170921000084417'
BAIDU_APP_KEY = '9ZlBKtiexIS5OObTp3GH'