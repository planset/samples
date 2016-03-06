import os
from flask import Flask, request, session, g, \
    redirect, url_for, abort, render_template, flash, jsonify
from flask.ext.openid import OpenID
from flask.ext.sqlalchemy import SQLAlchemy

DEBUG = True
SECRET_KEY = 'openidsample'
databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'oidsample.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % databese_file

app = Flask(__name__)
app.config.from_object(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
db = SQLAlchemy(app)
oid = OpenID(app, os.path.join(os.path.dirname(__file__), 'openid'))

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    email = db.Column(db.String(200))
    openid = db.Column(db.String(200))

    def __init__(self, name, email, openid):
        self.name = name
        self.email = email
        self.openid = openid

@app.before_request
def lookup_current_user():
    g.user = None
    if 'openid' in session:
        g.user = User.query.filter_by(openid=session['openid']).first()

@app.route('/')
def show_index():
    return render_template('index.jade')

@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None:
        return redirect(oid.get_next_url())
    if request.method == 'POST':
        openid = request.form.get('openid')
        if openid:
            return oid.try_login(openid, ask_for=['email', 'fullname', 'nickname'])
    return render_template('login.jade', next=oid.get_next_url(),
                           error=oid.fetch_error())

@app.route('/login_google', methods=['GET', 'POST'])
@oid.loginhandler
def login_google():
    openid = 'https://www.google.com/accounts/o8/id'
    return oid.try_login(openid, ask_for=['email', 'fullname', 'nickname'])

@oid.after_login
def create_or_login(resp):
    session['openid'] = resp.identity_url
    user = User.query.filter_by(openid=resp.identity_url).first()
    if user is not None:
        flash(u'Successfully signed in')
        g.user = user
        return redirect(oid.get_next_url())
    return redirect(url_for('create_profile', next=oid.get_next_url(),
                            name=resp.fullname or resp.nickname,
                            email=resp.email))

@app.route('/create-profile', methods=['GET', 'POST'])
def create_profile():
    if g.user is not None or 'openid' not in session:
        return redirect(url_for('show_index'))
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        if not name:
            flash(u'Error: you have to provide a name')
        elif '@' not in email:
            flash(u'Error: you have to enter a valid email address')
        else:
            flash(u'Profile successfully created')
            db.session.add(User(name, email, session['openid']))
            db.session.commit()
            return redirect(oid.get_next_url())
    return render_template('create_profile.jade', next_url=oid.get_next_url())

@app.route('/logout')
def logout():
    session.pop('openid', None)
    flash(u'You were signed out')
    return redirect(oid.get_next_url())

if __name__ == '__main__':
    app.run(host="0.0.0.0")
