from flask import Flask, render_template
from flask.ext.scss import Scss


app = Flask(__name__)

app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

app.debug = True
Scss(app)
#Scss(app, static_dir='static', asset_dir='assets') # default arguments

@app.route('/')
def index():
    return render_template('index.jade')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


