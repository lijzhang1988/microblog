from app.models.models import Users,Posts
from app.models import session

user = Users()
post = Posts()
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


users = session.query(Users.id,Users.username,Users.password,Users.nickname,Users.email,Users.imgpath,Users.last_seen).all()
print(users)


#posts = session.query(Posts.id,Posts.body,Posts.timestamp,Posts.user_id).all()
#print(posts)


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


#delete all posts
posts = session.query(Posts).all()
for post in posts:
    session.delete(post)
    session.commit()
    session.close()
