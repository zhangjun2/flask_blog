from flask_mail import Mail, Message

from webapp import app

MAIL_SERVER = 'smtp.qq.com',
MAIL_PROT = 25,
MAIL_USE_TLS = True,
MAIL_USE_SSL = False,
MAIL_USERNAME = "512269813@qq.com",
MAIL_PASSWORD = "zhangjun911206",
MAIL_DEBUG = True



mail = Mail(app)

@app.route('/')
def index():
    # sender 发送方哈，recipients 邮件接收方列表
    msg = Message("Hi!This is a test ",sender='example@example.com', recipients=['512269813@qq.com'])
    # msg.body 邮件正文
    msg.body = "This is a first email"
    # msg.attach 邮件附件添加
    # msg.attach("文件名", "类型", 读取文件）
    with app.open_resource("F:\2281393651481.jpg") as fp:
        msg.attach("image.jpg", "image/jpg", fp.read())

    mail.send(msg)
    print ("Mail sent")
    return "Sent"

def send_mail(body,sender,recipients,html=None,file=None):
    msg = Message(body,sender,recipients)
    msg.body = body
    mail.send(msg)