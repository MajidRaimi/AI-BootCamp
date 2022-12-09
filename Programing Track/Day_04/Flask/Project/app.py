from flask import Flask , render_template , request , redirect, url_for

app = Flask(__name__) # ! __name__ = __main__


@app.route('/') 
def index() : 
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/auth' , methods = ['POST' , 'GET'])
def auth():
    
    try : 
        if request.method == 'GET':
            username = request.args.get('username')
            password = request.args.get('password')
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            if username == 'admin' and password == 'admin':
                return render_template('welcome.html' , user = 'Admin')
            else :
                return render_template('login.html' , error = 'could not login')
    except Exception as e:
        print(e)
    
    return redirect(url_for('login'))

    

if __name__ == '__main__':
    app.run(debug=True)