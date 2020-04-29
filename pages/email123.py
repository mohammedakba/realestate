import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login('divumeh100@gmail.com', 'king@2020')
server.sendmail('imadsab33ayu@gamil.com', 'text mail', 'simple mssages')
