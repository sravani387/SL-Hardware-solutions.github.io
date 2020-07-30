from flask import Flask,redirect,url_for,render_template
app = Flask(__name__,template_folder='templates')
@app.route("/home")
def home():
       return render_template("index1.html")
    
@app.route('/admin')
def admin():
    return redirect(url_for('home'))
if __name__=='__main__':
    app.run()
    
