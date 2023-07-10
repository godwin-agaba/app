from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField,SubmitField


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(Form):
      name = StringField('What is your name?')
      submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500        

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/user/", methods=['GET','POST'])
def user():
    name = None
    form = NameForm()
    if form.validate_on_submit():
       name = form.name.data
       form.name.data = ''
    return render_template('index.html', form=form, name=name)

if __name__ == "__main__":
    app.run(debug=True)