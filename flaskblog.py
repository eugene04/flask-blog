from flask import Flask , render_template , url_for, flash, redirect
from forms import RegisrationForm,LoginForm 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b99a28f432'

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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title='login', form=form) 
    
    
    
    
if __name__ == "__main__":
    app.run(debug=True)


