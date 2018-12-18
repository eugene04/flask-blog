from flask import Flask , render_template , url_for
app = Flask(__name__)
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
    
    
    
if __name__ == "__main__":
    app.run(debug=True)


