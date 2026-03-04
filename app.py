import os
from flask import Flask, render_template, request, redirect, url_for, session
from assessment.routes import assessment_bp
import json

app = Flask(__name__)
app.secret_key = 'super_secret_key'
app.register_blueprint(assessment_bp, url_prefix='/assessment')

# Load users
def load_users():
    if not os.path.exists("users.json"):
        with open("users.json", "w") as f:
            json.dump({}, f)
    with open("users.json", "r") as file:
        return json.load(file)

# Save users
def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = load_users()

        if username in users:
            return 'User already exists'

        # Add new user with empty progress
        users[username] = {
            "password": password
            }

        save_users(users)
        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = load_users()
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('success'))
        return "Invalid credentials"
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    username = session.get('username')
    if not username:
        return redirect('/login')

    users = load_users()

    return render_template('dashboard.html', username=username)

@app.route('/learn/networking')
def learn_networking():
    if 'username' in session:
        return render_template("networking.html")
    return redirect('/login')

@app.route('/learn/encryption')
def learn_encryption():
    return render_template('encryption.html')

@app.route('/learn/hacking')
def ethical():
    return render_template('ethical.html')

@app.route('/learn/cybersecurity')
def cybersecurity():
    return render_template("cybersecurity.html")

@app.route('/learn/linux')
def linux():
    return render_template('linux.html')

@app.route('/learn/os_security')
def os_security():
    return render_template('os_security.html')

@app.route('/questions')
def questions():
    return render_template('questions.html')
# ================= CYBERHUB MODULE =================

@app.route('/cyberhub')
def cyberhub_home():
    if 'username' in session:
        return render_template('cyberhub_home.html')
    return redirect('/dashboard')

@app.route('/cyberhub/beginner')
def cyberhub_beginner():
    if 'username' in session:
        return render_template('beginner.html')
    return redirect('/login')

@app.route('/cyberhub/intermediate')
def cyberhub_intermediate():
    if 'username' in session:
        return render_template('intermediate.html')
    return redirect('/login')

@app.route('/cyberhub/advanced')
def cyberhub_advanced():
    if 'username' in session:
        return render_template('advanced.html')
    return redirect('/login')

@app.route('/cyberhub/tools')
def cyberhub_tools():
    if 'username' in session:
        return render_template('tools.html')
    return redirect('/login')

@app.route('/cyberhub/labs')
def cyberhub_labs():
    if 'username' in session:
        return render_template('labs.html')
    return redirect('/login')

@app.route('/cyberhub/certs')
def cyberhub_certs():
    if 'username' in session:
        return render_template('certs.html')
    return redirect('/login')  

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/success')
def success():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    return render_template('success.html', username=username)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
