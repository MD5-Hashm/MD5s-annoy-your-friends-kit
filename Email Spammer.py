import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = 'Insert Email here'
password = 'Insert Password here'
send_to_email = input('What email would you like to spam?: ') 
subject = 'Hello'
message = 'oof'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

count = 0

while True: 
    server = smtplib.SMTP('smtp.gmail.com', 587)    
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    count = count + 1 
    countstr = str(count)
    print(countstr + " Messages sent to " + send_to_email)
    server.quit()
