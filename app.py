from flask import Flask,render_template,redirect,request,session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.secret_key='yewin'
# database
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:root@localhost:5432/CycleTicket"
db=SQLAlchemy(app)
migrate = Migrate(app, db)
#table
class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100),unique=True,nullable=False)
    password=db.Column(db.String(100))
# route
@app.route('/')
def index():  # put application's code here
    return redirect('/home')

@app.route('/home')
def home():  # put application's code here
    if session and session['username']:
        return render_template('home.html',data={'user_session':session['username']})
    return render_template('home.html')

@app.route('/login', methods=['POST','GET'])
def login():  # put application's code here
    if request.method=='POST':
        name=request.form['username']
        pwd=request.form['password']
        user=Users.query.filter_by(username=name).first()
        data={'user':{'username':name,'password':pwd}}
        if not(user):
            data['status'] = 'fail'
            data['message'] = 'Log In Fail! There are problem with username.'
            data['username_err'] = 'Username does not exist.'
        elif user.password!=pwd:
            data['status'] = 'fail'
            data['message'] = 'Sign Up Fail! There are problem with the password you entered.'
            data['password_err'] = 'Password does not match.'
        else:
            session['username']=user.username
            return redirect('/home')
        return render_template('login.html',data=data)
    return render_template('login.html')

@app.route('/signup', methods=['POST','GET'])
def signup():  # put application's code here
    if request.method=='POST':
        name=request.form['username']
        pwd=request.form['password']
        con_pwd=request.form['confirm-password']
        user=Users.query.filter_by(username=name).first()
        data={'user':{'username':name,'password':pwd,'confirm_password':con_pwd}}
        if user:
            data['status']='fail'
            data['message']='Sign Up Fail! There are problem with username.'
            data['username_err']='Username already exist.'
        elif pwd!=con_pwd:
            data['status']='fail'
            data['message']='Sign Up Fail! There are problem with password.'
            data['password_err']='Password not match.'
        else:
            user=Users(username=name,password=pwd)
            db.session.add(user)
            db.session.commit()
            data['status']='success'
            data['message']="Sign Up Successfully with username \'"+name+"\'! Please Log In."
        return render_template('signup.html',data=data)
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username',False)
    return redirect('/home')

if __name__ == '__main__':
    app.run(debug=True)
