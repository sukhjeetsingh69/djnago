from flask import Flask,render_template,request,redirect
import mysql.connector
conn=mysql.connector.connect(host="localhost",username="root",password="root",database="school")

x=conn.cursor()



app = Flask(__name__)




@app.route("/")
def home():
    return render_template("base.html")

@app.route("/about")
def about():
    return render_template("about.html")
    

@app.route("/contact")
def contact():
    return render_template("contact.html")
    

@app.route("/show")
def show():
    return render_template("show.html")

@app.route("/saveinfo",methods=["POST"])    
def saveinfo():
    if request.method=="POST":
        
        tou=request.form.get("abc")
        pop=request.form.get("dfg")

        print(tou)
        print(pop)
        x.execute("insert into teacher(Title,Description) values(%s, %s)",(tou,pop))
        conn.commit()
        return redirect("/contact")
#hlooo


if __name__ == '__main__':
    app.run(debug=True)
