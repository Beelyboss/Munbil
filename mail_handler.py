# mail_handler.py
from flask_mail import Mail, Message
from config import Config

mail = Mail()

def configure_mail(app):
    app.config.from_object(Config)
    mail.init_app(app)

def send_verification_email(to_email, verification_code):
    subject = 'Email Verification Code'
    body = f'Your verification code is: {verification_code}'
    message = Message(subject=subject, recipients=[to_email], body=body)
    mail.send(message)