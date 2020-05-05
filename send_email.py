import smtplib
import mysql.connector
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
mydb=mysql.connector.connect(user='root',host='localhost',password='amul7155',db='pythonproject')
cursor=mydb.cursor()
cursor.execute("select * from python_proj")
l=[]
for i in cursor.fetchall():
    print (i)
    l.append(i[2])
print (l)
mydb.commit()
mydb.close()
email_user = input("enter the email id")
email_password = input("enter the password")
email_send =l
    
subject = 'sub: sending mails through python'
    
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = ",".join(l)
msg['Subject'] = subject
    
body = 'hey all how are you!'
msg.attach(MIMEText(body,'plain'))
    
filename="F:/python/datasetofpython.csv"
attachment  =open(filename,'rb')
        
part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)
        
msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()