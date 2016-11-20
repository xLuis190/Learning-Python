from flask import *
import mysqlcon
app = Flask(__name__)
port = '80'

@app.route('/')
def hello_world():
    return render_template('index.html');

@app.route('/post', methods=['GET', 'POST'])
def post_request():
    if request.method == "POST":
        print(request.form["name"]);

    return render_template('index.html');

try:
    with connection.cursor() as cursor:
        sql = "SELECT `phoneNumber`, `Adress` FROM `test` WHERE `userName`=%s"
        cursor.execute(sql, ('webmaster@python.org'));
        print(cursor.fetchone());
finally:
    connection.close();
print ("running on port"+port)
app.run("0.0.0.0",port=port);
