from flask import render_template, request, Blueprint, flash
from flask_mail import Message
from tutorial.models import Post
from tutorial import mail
import cryptocompare


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route('/about')
def about():
    return render_template('about.html', title='About')


btc = cryptocompare.get_price(['BTC'], ['EUR', 'GBP', 'USD'])


@main.route('/crypto')
def crypto():
    return render_template('crypto.html', title='Crypto', btc=btc)


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        msg = Message(subject,
                      sender='noreply@demo.com',
                      recipients=['hacivat_444@hotmail.com'])
        msg.body = f""" Sender name;{name}\nSender email; {email}\n \n{request.form['text']} """
        msg.html = f'<b> {msg.body} </b>'
        mail.send(msg)
        flash('Mail has been sent! I will be in touch!', 'success')

    return render_template('contact.html', title='Contact Us')
