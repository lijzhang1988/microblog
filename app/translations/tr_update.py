import os

pybabel = '/opt/python/new_vir/bin/pybabel'
os.chdir('/root/PycharmProjects/microblog/app')
os.system(pybabel + ' extract -F babel.cfg -k lazy_gettext -o messages.pot app')
os.system(pybabel + ' update -i messages.pot -d translations')

