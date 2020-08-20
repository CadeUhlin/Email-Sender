import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Cade Uhlin'
email['to'] = '<email address that will receive the email>'
email['subject'] = 'Prize Money'

email.set_content(html.substitute({'name': 'name of the person receiving the email'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('<sender email address>', '<email password from the sender>')
    smtp.send_message(email)
    print('all good boss!')
