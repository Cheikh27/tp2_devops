from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Simulate a user database
users = {'cheikh': 'password123'}

# Route to display the splash screen
@app.route('/')
def splash_screen():
    return render_template('index.html')

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('home'))
        else:
            return "Invalid credentials, try again."
    return render_template('login.html')

# Route for registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            users[username] = password
            return redirect(url_for('login'))
        else:
            return "User already exists."
    return render_template('register.html')

# Route for home page after login
@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
