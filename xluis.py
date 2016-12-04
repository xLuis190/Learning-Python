from flask import Flask, render_template,request,url_for;

app = Flask(__name__);

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/post',methods=['POST'])
def post_request():
    if request.method == "POST":
        print(request.form['username'])
    return request.form['username'];

app.run(port=80)
