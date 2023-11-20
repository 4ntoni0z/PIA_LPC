#Juan Antonio Sena Castillo
#1973595
#Grupo 062


#Se importa las librerias 
import smtplib
import os 
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

remitente= "senacastillo3@gmail.com"#Se define el correo que va enviar la informacion
destinatario= "gerardo.bernal@uanl.edu.mx"#receptor de la informacion
asunto="Pueba de envio script python 1973595"#Asunto del correo

#se alamacena la informacion en la funcion msg pasada para que se puede enviaren el correo
msg= MIMEMultipart()
msg['Subject']=asunto
msg['From']=remitente
msg['To']=destinatario

#se usa html para crear el cuerpo del correo
html = """
    <html>
    <body>
        <H1> Prcatica 12 </H1>
        <a>Ejercicio de la practica 12 de envio de correos</a><br><br>
        <a>Nombre: Juan Antonio Sena Castillo</a> <br><br>
        <a>Matricula: 1973595</a> <br><br>
    </body>
    </html>
    """
    

#Se almacena pen la funcion msg para enviar el correo    
msg.attach(MIMEText(html, 'html'))

#se define la ruta de la image
image_path = "fcfm_cool.png"
#se abre el archivo para almacenarlo en la funcion msg
with open(image_path, "rb") as image_file:
    image = MIMEImage(image_file.read(), name="imagen.png")
    msg.attach(image)


conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
#se envia el correo
conn.starttls()
conn.login('senacastillo3@gmail.com','')#Añadir el password
conn.sendmail(remitente,destinatario,msg.as_string(),)
#se cierra la funcion
conn.quit
