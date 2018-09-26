# from flask.ext.mysql import MySQL
from flaskext.mysql import MySQL
# from werkzeug import generate_password_hash, check_password_hash
from flask import Flask, render_template, json, request,redirect,session
app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'thisari123'
app.config['MYSQL_DATABASE_DB'] = 'sensei'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def main():
    return render_template('sensei.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST'])
def signUp():
    # read the posted values from the UI
    _firstname = request.form['inputFirstName']
    _lastname = request.form['inputLastName']
    _faculty = request.form['inputFaculty']
    _university = request.form['inputUniversity']
    _linkedin = request.form['inputLinkedin']
    _researchgate = request.form['inputResearchGate']
    _username = request.form['inputUsername']
    _password = request.form['inputPassword']


    # validate the received values
    if _firstname and _faculty and _username and _password:
        conn = mysql.connect()
        cursor = conn.cursor()

        # _hashed_password = generate_password_hash(_password)
        cursor.callproc('sp_createCredentials', (_username, _password))

        data = cursor.fetchall()

        if len(data) is 0:
            conn.commit()
        else:
            return json.dumps({'error': str(data[0])})

        conn1 = mysql.connect()
        cursor1 = conn1.cursor()
        cursor1.callproc('sp_getUser', (_username,))
        data1 = cursor1.fetchall()

        if len(data1) > 0:
            id = data1[0][0]
            conn2 = mysql.connect()
            cursor2 = conn2.cursor()
            cursor2.callproc('sp_createAcademic', (id, _firstname, _lastname, _faculty, _university, _linkedin, _researchgate))

            data2 = cursor.fetchall()

            if len(data2) is 0:
                conn2.commit()
                return json.dumps({'message': 'Academic added successfully !'})
            else:
                return json.dumps({'error': str(data2[0])})


        # if len(data) is 0:
        #     conn.commit()
        #     return json.dumps({'message': 'User created successfully !'})
        # else:
        #     return json.dumps({'error': str(data[0])})

        # return json.dumps({'html': '<span>All fields good !!</span>'})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

if __name__ == "__main__":
    app.run()