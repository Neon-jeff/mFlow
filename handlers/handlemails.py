from django.conf import settings
import smtplib
from django.template.loader import render_to_string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings
import base64
import requests


sender=settings.EMAIL_USER
auth=settings.EMAIL_AUTH

def SendOTPEmail(user,otp):
    recipient = f'{user.email}'
# Create message
    msg = MIMEMultipart("alternative")
    email_template=render_to_string('emails/otp-email.html',{'user':'','otp':otp})
    # text="Hi, welcome to nello"
    msg['Subject'] = f"Verify your account"
    msg['From'] = sender
    msg['To'] = recipient
    part2 = MIMEText(email_template, 'html')
    msg.attach(part2)
# Create server object with SSL option
    server = smtplib.SMTP_SSL("smtp.zoho.com", 465)
# Perform operations via server
    server.login(sender, auth)
    server.sendmail(sender, [recipient], msg.as_string())
    server.quit()


def SendSubEmail(user,plan):
    recipient = f'{user.email}'
# Create message
    msg = MIMEMultipart("alternative")
    email_template=render_to_string('emails/subscription.html',{'user':user,'plan':plan})
    # text="Hi, welcome to nello"
    msg['Subject'] = f"Subscription Verified"
    msg['From'] = sender
    msg['To'] = recipient
    part2 = MIMEText(email_template, 'html')
    msg.attach(part2)
# Create server object with SSL option
    server = smtplib.SMTP_SSL("smtp.zoho.com", 465)
# Perform operations via server
    server.login(sender, auth)
    server.sendmail(sender, [recipient], msg.as_string())
    server.quit()

