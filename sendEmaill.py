# coding = utf -8
import smtplib
from email.mime.text import MIMEText
def send(titlt_,content_):
    #设置服务器所需信息
    #163邮箱服务器地址
    mail_host = 'smtp.163.com'
    #163用户名（正常情况下是@前面的部分）
    mail_user = 's18961489072'
    #密码  这里要的是开启后的授权码
    mail_pass = 'ADKBYFFMJDSNDJKY'
    #邮件发送方邮箱地址
    sender = 's18961489072@163.com'
    #邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = ['stx0529@163.com']


    #设置email信息
    #邮件内容设置
    message = MIMEText(content_,'plain','utf-8')
    #邮件主题
    message['Subject'] = titlt_
    #发送方信息
    message['From'] = sender
    #接受方信息
    message['To'] = receivers[0]


    try:
        # smtp协议的默认端口是25，QQ邮箱smtp服务器端口是465,
        # 第一个参数是smtp服务器地址，第二个参数是端口，
        # 第三个参数是超时设置,qq邮箱必须使用ssl证书，要不链接不上服务器，但是163不用
        server = smtplib.SMTP()
        server.connect(mail_host,25)
        # 登录邮箱
        server.login(mail_user,mail_pass)
        # 发送邮件，第一个参数是发送方地址，
        # 第二个参数是接收方列表，列表中可以有多个接收方地址，表示发送给多个邮箱
        # msg.as_string()将MIMEText对象转化成文本
        server.sendmail(sender, message['To'], message.as_string())
        server.quit()
        print ('success')

    except Exception as e:
        return  f'Faild:%{e}'

    return 'success'