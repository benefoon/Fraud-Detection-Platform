import smtplib
from email.mime.text import MIMEText

# Send email notification
def send_email(subject, body, to_email):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = to_email

    with smtplib.SMTP('smtp.example.com') as server:
        server.login('your_email@example.com', 'password')
        server.sendmail(msg['From'], msg['To'], msg.as_string())
      
