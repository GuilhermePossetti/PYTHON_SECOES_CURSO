# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/35514874#content
# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/15355208#content


# Enviando E-mails SMTP com Python

import os
import pathlib
import smtplib
from string import Template
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv # type: ignore


load_dotenv()


# Caminho arquivo HTML

CAMINHO_HTML = pathlib.Path(__file__).parent / 'aula24_enviando_emails.html'




# Dados do remetente e destinatário
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente 



# Config SMTP

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')



# Mensagem de texto

with open(CAMINHO_HTML, 'r', encoding='utf-8') as arquivo:
    texto_arquivo= arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome="joao")



# Transformar nossa msg em MIMEMultipart

mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este é o assundo do e-mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)



# Envia o E-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso')