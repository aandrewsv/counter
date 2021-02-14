from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)  
app.secret_key = "admin"

@app.route("/")         
def index():
    if  'visits' in session:
        session['visits'] += 1
        return render_template("index.html")
    else:
        session['visits'] = 1
        return render_template("index.html")

@app.route("/add2")
def add2():
    session['visits'] += 1
    return redirect("/")

@app.route("/destroy")
def destroy():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

