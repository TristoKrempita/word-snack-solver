from flask import Flask,url_for,render_template, request, flash
from words import word_finder
app = Flask(__name__)
app.secret_key = "asd"

@app.route("/",methods=['GET','POST'])
def words():
    if request.method == "POST":
        if not(request.form['letters'].isalpha()):
            flash("Only input letters please")
            return render_template('home.html')
        print(request.form['letters'])
        words_dict = word_finder(request.form['letters'])
        return render_template('home.html',words = words_dict)
    return render_template('home.html')
