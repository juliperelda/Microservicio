import json
from wsgiref.simple_server import make_server
import os
import sys
import smtplib 

def envioMail(): # Funcion de envio de mail.
    mail_user= 'juliperelda@outlook.com'
    mail_pass = 'juli40928607'
    FROM = 'juliperelda@outlook.com'
    TO = "juliperelda@gmail.com" if type("juliperelda@gmail.com") is list else ["juliperelda@gmail.com"]
    SUBJECT = "Envio de mail - Prueba Microservicio"
    TEXT = "Esto es un mail de prueba, esperemos que haya llegado rey ;)"

    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.outlook.com", 587)
        server.ehlo()
        server.starttls()
        server.login(mail_user, mail_pass)
        server.sendmail(FROM, TO, message)
        server.close()
        print('!Correo enviado!')
    except:
      print('!Error al enviar correo!')


def hello_world_app(environ, start_response):
    # print(environ) # Obtengo entorno de variables que recupero de la request.
    res = os.path.join(path, environ["PATH_INFO"][1:]) # Se obtiene la ruta.
    status = '200 OK'  # HTTP Status

    headers = [('Content-type', 'application/json; charset=utf-8')] # HTTP Headers
    start_response(status, headers) # Configuracion de headers

    # Con la ruta recuperada validamos el nombre del endpoints que queremos que se ejecute.
    if ( res.rsplit('/', 1)[1] == "envioMail"): 
        envioMail() # Funcion envio de mail

        response = {
            'mensaje': 'Envio de mail exitoso'
        }
    else: 
        response = {
            'mensaje': 'Microservicio funcionando' # Valido que el microservicio funciona
        }


    return [ bytes(json.dumps(response), 'utf-8') ] # Devuelve respuesta del response.


with make_server('', 8001, hello_world_app) as httpd: # Server
    print("Serving on port 8001")
    path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd() #Obtengo el path
    

    # Para que se mantenga corriendo.
    httpd.serve_forever()
