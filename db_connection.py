from app.models.models import Users
from app.models import session

user = Users()
#user.username = 'lijzhang'
#user.password = 'zaq12wsx'
#user.nickname = 'ZLJ'
#user.email = 'lijzhang@cn.ibm.com'
#user.description = 'This is a test user'
#session.add(user)
#user = Users()
#user.username = 'zzz'
#user.password = 'zaq12wsx'
#user.nickname = 'ZLJ'
#user.email = 'zzz@cn.ibm.com'
#user.description = 'This is a test user'
#session.add(user)
#session.commit()
#session.close()


users = session.query(Users).all()
print(users)

#user = session.query(Users).get(1)
#print(user)

#user.password = 'xsw22edc'
#session.add(user)
#session.commit()
#session.close()

#users_f = session.query(Users).filter_by(username='lijzhang').all()
#print(users_f)

#user = session.query(Users).get(3)
#print(user)
#session.delete(user)
#session.commit()
#session.close()

#users = session.query(Users).all()
#print(users)