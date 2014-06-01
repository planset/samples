#!/usr/bin/env python
# -*- encoding:utf8 -*-
from flask import Flask, Response, json, render_template
from flask import request
application = Flask(__name__)

def jsonp(data, callback="function"):
    return Response(
        "%s(%s);" %(callback, json.dumps(data)),
        mimetype="text/javascript"
        )

@application.route("/api")
def api():
    data = {"content":"hogehoge"} # 辞書型のデータ作る
    callback = request.args.get("callback")
    if callback:
        return jsonp(data, callback)
    return jsonp(data)

@application.route("/")
def index():
    return "aplication working!"

@application.route("/aa")
def aa():
    return render_template("aa.html")

if __name__ == "__main__":
    application.run()

