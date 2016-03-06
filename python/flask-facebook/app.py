# -*- coding: utf-8 -*-
from flask import (Flask, render_template, redirect, url_for, request, g, session,
                  abort)
from myfacebook import Facebook
from functools import wraps
import datetime

app = Flask(__name__)
app.secret_key = "agjerjgklaerhglanerihlahgaelburhgl"

fb_app_key = "115583065169378"
fb_secret_key = "f599439601e96496965668e8676035c7"
callback_uri = "http://localhost:5000/connect/fb/callback/"
scope = ['email','user_notes', 'create_note']


def requires_oauth_fb(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not g.fb.is_authorized():
            return abort(401)
            #return redirect(url_for('connect_fb'))

        return f(*args, **kwargs)
    return decorated_function


@app.route("/favicon.ico")
def get_favicon():
    return app.send_static_file('favicon.ico')

def _not_requires_oauth_fb():
    if request.path in ["/favicon.ico"]:
        return True
    
@app.before_request
def build_facebook():
    if _not_requires_oauth_fb():
        return
        
    g.fb = Facebook(fb_app_key, fb_secret_key, callback_uri, scope=scope)
    
    fb_access_token = session.get('fb_access_token', None)
    fb_expires = session.get('fb_expires', None)
    fb_id = session.get('fb_id', None)
    fb_name = session.get('fb_name', None)
    try:
        g.fb.set_token(fb_access_token)
    except Facebook.NotAuthorizedTokenException:
        _clear_fb_session()
        return redirect(url_for('connect_fb'))

    g.ctx = {}
    g.ctx["is_loggedin"] = not (fb_name is None)
    g.ctx["user_name"] = fb_name
    

@app.route("/")
def index():
    if g.fb.is_authorized():
        g.ctx["profile"] = g.fb.me()
        g.ctx["friends"] = g.fb.me_friends()
        return render_template("index.html", **g.ctx)
    
    return render_template("index.html")
    

def _clear_fb_session():    
    del session["fb_access_token"]
    del session["fb_expires"]
    del session["fb_id"]
    del session["fb_name"]

def _redirect_fb_oauth_login_url(next_url=None):
    if next_url:
        session["next_url"] = next_url
    return redirect(g.fb.oauth_login_url())
    
@app.route("/connect/fb/")
def connect_fb():
    next_url = _get_next_url()
    return _redirect_fb_oauth_login_url(next_url=next_url)

@app.route("/connect/fb/callback/")
def connect_fb_callback():
    code = request.args.get("code", None)
    if code is None:
        return redirect(url_for('login'))

    (access_token, expires) = g.fb.fbapi_auth(code)
    session["fb_access_token"] = access_token
    
    now = datetime.datetime.now()
    expire = now + datetime.timedelta(seconds=int(expires))
    session["fb_expires"] = str(expire)
    
    profile = g.fb.me()
    session["fb_id"] = profile["id"]
    session["fb_name"] = profile["name"]
    
    next_url = session.get("next_url", None)
    if next_url:
        del session["next_url"]
        return redirect(next_url)
    
    return redirect(url_for('index'))

@app.route("/logout/fb/")
def logout_fb():
    """
    実際にfacebookからログアウトするわけではない。セッション変数を破棄するだけ。
    """
    _clear_fb_session()
    
    next_url = request.args.get("next_url", None)
    if not next_url:
        next_url = request.headers["Referer"]
        
    return redirect(next_url)
    #return redirect(g.fb.logout_url())

@app.route("/note/")
@app.route("/note/list")
@requires_oauth_fb
def list_note():
    g.ctx["notes"] = g.fb.me_notes()
    return render_template("note_list.html", **g.ctx)
    
@app.route("/note/<id>")
def detail_note(id):
    g.ctx["note"] = g.fb.get_note(id)
    g.ctx["next_url"] = request.url
    return render_template("note_detail.html", **g.ctx)

def _get_next_url():
    next_url = request.values.get("next_url", None)
    print next_url
    if not next_url:
        next_url = request.headers.get("Referer", None)
    return next_url
        
@app.route("/note/add/", methods=["GET", "POST"])
@requires_oauth_fb
def add_note():
    if request.method == "GET":
        return render_template("note_add.html", **g.ctx)
    else:
        next_url = _get_next_url()
        id = request.form.get("id")
        subject = request.form.get("subject")
        message = request.form.get("message")
        g.fb.save_note(id, subject, message)
        if next_url:
            return redirect(next_url)
        return render_template("note_add.html")

    
if __name__ == "__main__":
    app.run(debug=True)

