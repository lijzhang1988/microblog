from flask_mail import Message
from app import app, mail
from app.config import ADMINS
msg = Message('test subject',sender=ADMINS[0],recipients=ADMINS)
msg.body = 'test body'
msg.html = '<b>HTML</b> body'
with app.app_context():
    mail.send(msg)