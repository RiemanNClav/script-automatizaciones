import smtplib
from email.message import EmailMessage

def send_email(asunto, body: str, correo_emisor: str,  correos_destinatarios: list):
    email = EmailMessage()
    email.set_content(body)
    email['Subject'] = asunto
    email['From'] = correo_emisor
    email['To'] = ', '.join(correos_destinatarios)

    # Conexión al servidor SMTP de Gmail
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()  # Encriptamos la conexión
        smtp.login(correo_emisor, 'Marmansanico12345')  # Iniciar sesión
        smtp.send_message(email)  # Enviar el correo

# Lista de destinatarios
destinatarios = ['pyrat.solutions@gmail.com']

# Llamada a la función
send_email('Recordatorio Importante',  'No olvides la reunión de mañana a las 3pm.', 'angel.chavez.clavellina@gmail.com', destinatarios)

print('Lo correos se enviaron con exito')
