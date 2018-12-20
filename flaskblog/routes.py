from flask import  render_template , url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegisrationForm,LoginForm 
from flaskblog.models import User, Post


posts=[
{
    'author':'eugene jemwa',
    'title':'1st post',
    'content':'first post content',
    'date_posted':'December 18 2018'

},
{
    'author':'gari jemwa',
    'title':'2nd post',
    'content':'second post content',
    'date_posted':'December 28 2018'

}



]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html' , posts=posts) 

@app.route("/about")
def about():
    return render_template('about.html',title='about') 

@app.route("/register",methods = ['GET','POST'])
def register():
    form = RegisrationForm() 
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('your account has been created you are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='register', form=form)

@app.route("/login",methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('you have been logged in', 'success')
            return redirect(url_for('home')) 
        else:
            flash('login Unsuccesful.Please check password and email', 'danger')
    return render_template('login.html',title='login', form=form) 
    
    