from flask import render_template, Flask,url_for, redirect
from flask_mail import Mail, Message

app = Flask(__name__)


# App.config all config values listed below should be in a .env file  and accessed using os.environ.get(value)
app.config['DEBUG'] = False
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = "joseph05fagua@gmail.com"
app.config['MAIL_PASSWORD'] = "eucwekaaafjaihxz"
app.config['MAIL_DEFAULT_SENDER'] = ("Joseph From GoCreattivo","joseph05fagua@gmail.com") #For the email to be sent with a from for the sender it must be in a tuple that includes a small name or message followed by the actual from email
app.config['MAIL_MAX_EMAILS'] = None # This blocks the mail system to make it stop once it reaches the max emails sent and will create a new connection and continue sending emails
app.config['MAIL_ASCII_ATTACHMENTS'] = False
mail = Mail(app)


# Message(f'Hey there,', sender=f'myname@myemail.com', recipients=['<EMAIL>'])
#       The first '' upon object declaration
#       is the Subject, if we use the sender we can define the sender just like the default
#       sender we did in the tuple with a message
# msg.html = '<b>This is a test email sent from Joseph\'s app.</b>'
#       This is for when we want to send custom email forms that look a certain way using html
#       the body and html can't be used together it will prioritize the html message
# msg = Message(
#     subject='',
#     recipients=['xoxarej981@angewy.com'],
#     body='',
#     html='',
#     sender='',
#     cc=[],
#     bcc=[],
# )     This are some of the parameters the msg object can have for sending emails
@app.route('/', methods=['GET'])
def index():
    return render_template("ContactForm-1.html")


@app.route('/contact', methods=[ 'POST'])
def submit_form():
    msg = Message(f'Hey there,', recipients=['xoxarej981@angewy.com'])
    msg.body = 'This is a test email sent from Joseph\'s app.'
    mail.send(msg)
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()