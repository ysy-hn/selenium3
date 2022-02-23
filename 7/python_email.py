import smtplib
from email.mime.text import MIMEText
from email.header import Header


# 发送邮件主题
subject = "python email test"

# 编写Html类型的邮件正文
msg = MIMEText('<html><h1>您好！</h1></html>', 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect("smtp.126.com")
smtp.login('sender@126.com', 'a123456')
smtp.sendmail('sender@126.com', 'receriver@126.com', msg.as_string())
smtp.quit()

