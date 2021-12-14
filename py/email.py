import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 

msg = MIMEMultipart()
message = "BackUp Terminal Annanda Terminado"
password_email = "SenhaDoEmail"

msg['Subject'] = "Assunto E-mail" #assunto
msg['From'] = "E-mail de envio"
msg['To'] = "E-mail de recebimento"

 

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com: 587') #Servidor de envio do Gmail
 
server.starttls()
server.login(msg['From'], password_email)

server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print ("E-mail enviado com sucesso, script finalizado")