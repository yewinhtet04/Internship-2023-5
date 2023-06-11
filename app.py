from flask import Flask,render_template,redirect,request,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
#from flask_migrate import Migrate
from img2txt import extract_data
from data import price,payment_images,admin_username,admin_password

app = Flask(__name__)

app.secret_key='yewin'
# database
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:root@localhost:5432/CycleTicket"
db=SQLAlchemy(app)
#migrate = Migrate(app, db)
#table
class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100),unique=True,nullable=False)
    password=db.Column(db.String(100),default=db.false)

class Orders(db.Model):
    order_id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,nullable=False)
    tickets=db.Column(db.String(200),nullable=False)
    payment=db.Column(db.String(200))
    verify=db.Column(db.Boolean)
#created_at = db.Column(db.DateTime(timezone=True),server_default=func.now())
with app.app_context():
    db.create_all()


# route
@app.route('/')
def index():  # put application's code here
    return redirect('/home')

def get_session_user():
    if session and session.get('username'):
        return session.get('username')
    return None

@app.route('/home')
def home():  # put application's code here
    if get_session_user():
        user=Users.query.filter_by(username=get_session_user()).first()
        orders = Orders.query.filter(or_(Orders.verify==True , Orders.verify==None))
        print(orders)
        tickes={}
        for i in range(1,151):
            tickes.update({f"{i:03}":1})
        for ord in orders:
            ordered_ticket=ord.tickets.split(',')
            sts=0
            if ord.user_id==user.id:    sts=2
            for tic in ordered_ticket:
                tickes[tic]=sts
        return render_template('home.html',data={'user_session':get_session_user(),'tickes':tickes})
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
        '''Admin LogIn'''
        if name==admin_username and pwd==admin_password:
            session['admin_username']=admin_username
            return redirect('/admin')
        '''Admin LogIn'''
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
@app.route('/admin_logout')
def admin_logout():
    session.pop('admin_username',False)
    return redirect('/home')

@app.route('/order',methods=['POST'])
def order():
    if get_session_user():
        u_name=get_session_user()
        tickets=request.form['tickets']
        if not(tickets):
            return redirect('/home')
        count=len(tickets.split(','))
        prices=count* price
        data={'tickets':tickets,'user_session':u_name,'price':price,'quantity':count,'total_price':prices}
        return render_template('order.html',data=data)
    else:
        return redirect('/login')
from PIL import Image
import os.path
def create_filename(name):
    count=0
    tem_name=name
    word=name.split('.')
    while os.path.isfile(payment_images +tem_name):
        tem_name=word[0]+str(count)+'.'+word[1]
        count+=1
    return tem_name

@app.route('/buyticket',methods=['POST'])
def buyticket():
    if get_session_user():
        u_name=get_session_user()
        tickets=request.form['tickets']
        file=request.files['file']
        img=Image.open(file)
        if file.filename=='' or not(extract_data(img)):
            count = len(tickets.split(','))
            prices = count * price
            data = {'tickets': tickets, 'user_session': u_name, 'price': price, 'quantity': count,'total_price': prices,'ss_err':'Invalid screenshot! take it clear and try again.'}
            return render_template('order.html', data=data)
        #img.close()
        file_name=create_filename(file.filename)
        img.save(payment_images+file_name)
        #file.save(payment_images+file_name)
        # print(file,extract_data(Image.open(file)))
        user=Users.query.filter_by(username=u_name).first()
        order=Orders(user_id=user.id,tickets=tickets,payment=payment_images+file_name)
        db.session.add(order)
        db.session.commit()
        data={'status':'success','tickets':tickets,'user_session':u_name,}
        return render_template('buy_success.html',data=data)
    else:
        return redirect('/login')
@app.route('/profile')
def profile():
    if get_session_user():
        u_name=get_session_user()
        user=Users.query.filter_by(username=u_name).first()
        my_order=Orders.query.filter_by(user_id=user.id).order_by(Orders.order_id.desc())
        orders=[]
        count=1
        for o in my_order:
            tem=o.__dict__
            tem['num']=count;count+=1
            tem['price']=len(tem['tickets'].split(','))*price
            orders.append(tem)
        data={'user_session':u_name,'order':orders,'user':user}
        return render_template('profile.html',data=data)
    return redirect('/home')

def generate_data_for_admin(orders):
    my_order = [];
    count = 1
    for o in orders:
        tem = o.__dict__
        tem['username'] = Users.query.filter_by(id=tem['user_id']).first().username
        tem['num'] = count;
        count += 1
        tem['price'] = len(tem['tickets'].split(',')) * price
        img = Image.open(o.payment)
        tem['payment'] = extract_data(img)
        img.close()
        my_order.append(tem)
    return my_order

@app.route('/admin')
def admin():  # put application's code here
    if session and session.get('admin_username')==admin_username:
        orders = Orders.query.filter(Orders.verify == None)
        accept_orders = Orders.query.filter(Orders.verify == True).order_by(Orders.order_id.desc())
        reject_orders = Orders.query.filter(Orders.verify == False).order_by(Orders.order_id.desc())
        data={'admin_username':session.get('admin_username'),
              'pending_order':generate_data_for_admin(orders),
              'accepted_order':generate_data_for_admin(accept_orders),
              'rejected_order':generate_data_for_admin(reject_orders),}
        return render_template('admin.html',data=data)
    return redirect('/home')

@app.route('/admin_accept', methods=['POST'])
def admin_accept():
    order_id=request.form['order_id']
    result = Orders.query.filter_by(order_id=order_id).update(dict(verify=True))
    db.session.commit()
    return redirect('/admin')

@app.route('/admin_reject', methods=['POST'])
def admin_reject():
    order_id=request.form['order_id']
    result = Orders.query.filter_by(order_id=order_id).update(dict(verify=False))
    db.session.commit()
    return redirect('/admin')

if __name__ == '__main__':
    app.run(debug=True)
