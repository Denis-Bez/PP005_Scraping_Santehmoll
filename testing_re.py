from email.mime import application
import re
import csv
from datetime import datetime
from unittest import result
import time
from datetime import date
import json

from config import CONFIG
from flask import Flask
from flask_mail import Mail, Message

application = Flask(__name__)
application.config["SECRET_KEY"] = CONFIG["SECRET_KEY"]
application.config["MAIL_DEFAULT_SENDER"] = CONFIG["MAIL_DEFAULT_SENDER"]
application.config["MAIL_PASSWORD"] = CONFIG["MAIL_PASSWORD"]
application.config["MAIL_PORT"] = 465
application.config["MAIL_USE_TLS"] = False
application.config["MAIL_USE_SSL"] = True
application.config["MAIL_USERNAME"] = CONFIG["MAIL_USERNAME"]
mail = Mail(application)
application.app_context()

def repl():
    current_date = datetime.now()
    s_date = current_date.strftime('%d-%m-%Y %H:%M:%S')
    # with open("my1.log", 'a') as f:
    #     f.write(s_date + ' my dat\n')

    msg = Message(f"Script is working: {s_date}", recipients = ['v417459@yandex.ru'])
    msg.body = ('Test messange')
    a = mail.send(msg)
    print(a)

if __name__ == "__main__":
    application.run(debug=True) 
    repl()