import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.mime.message import MIMEMessage
from copy import deepcopy


class SMTP:
    def __init__(self):
        self.fromEmail="filoink@hyperchain.cn"
        self.toEmail="zhangrui@hyperchain.cn"
        self.SQM="inM5oaRuTSojWyc8"
    def sendEmail(self,filePathList,code:str):
        con = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
        con.login(self.fromEmail, self.SQM)
        msg = MIMEMultipart()
        subject = Header(code, 'utf-8').encode()
        msg['Subject'] = subject
        msg['From'] = self.fromEmail+" <"+self.fromEmail+">"
        msg['To'] = self.toEmail
        for filePath in filePathList:
            file1 = MIMEText(open(filePath, 'rb').read(), 'base64', 'utf-8')
            file1["Content-Disposition"] = 'attachment; filename='+os.path.basename(filePath).split('/')[-1]
            msg.attach(file1)
        # 发送邮件
        con.sendmail(self.fromEmail, self.toEmail, msg.as_string())
        con.quit()


