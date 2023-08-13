import smtplib 
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = '' # Name 
email['to'] = '' # Email address of receiver
email['subject'] = '' # Subject of email

email.set_content(html.substitute(name = ''), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('', '') # Email address of sender and password to account
	smtp.send_message(email)
	print('all good')