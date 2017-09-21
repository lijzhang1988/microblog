import os

pybabel = '/opt/python/new_vir/bin/pybabel'
os.chdir('/root/PycharmProjects/microblog/app')
os.system(pybabel + ' compile -d translations')

