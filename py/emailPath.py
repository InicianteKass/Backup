import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart()
message = "Mensagem do gmail" #Mensagem
password_email = "SenhaDoEmail"

msg['Subject'] = "Assunto" #assunto
msg['From'] = "E-mail de envio"
msg['To'] = "e-mail de recebimento"

msg.attach(MIMEText(message, 'plain'))

filename = 'LOGS.zip' 
attachment = open('LOG\LOGS.zip','rb') 

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    
msg.attach(part)
attachment.close()

server = smtplib.SMTP('smtp.gmail.com: 587') # Servidor de envio do Gmail
 
server.starttls()
server.login(msg['From'], password_email)

server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print ("E-mail enviado com sucesso, script finalizado")