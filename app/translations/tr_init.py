import os

pybabel = '/opt/python/new_vir/bin/pybabel'
os.chdir('/root/PycharmProjects/microblog/app')
os.system(pybabel + ' extract -F babel.cfg -k lazy_gettext -o messages.pot .')
os.system(pybabel + ' init -i messages.pot -d translations -l zh')
