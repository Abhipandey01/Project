from flask import Flask, render_template,request, jsonify


app = Flask(__name__)

@app.route("/" , methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')

@app.route("/e-learning")
def e_learning():
    return render_template('E-learning.html')

@app.route("/Course")
def Course():
    return render_template('Course.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")
