import smtplib

userName = input('ingrese su correo: ')
password = input('Clave correo: ')
destinatario = input('correo destino: ')
msg = input('Texto del mensaje: ')

server = smtplib.SMTP('smtp.gmail.com:535')
server.starttls()
server.login(userName, password)
server.sendmail(userName, destinatario, msg)
server.quit()

print('Correo enviado')
