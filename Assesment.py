from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['admin_panel']
users_collection = db['users']
databases_collection = db['databases']

# Login/Signup
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = users_collection.find_one({'username': username, 'password': password})
        if user:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = users_collection.find_one({'username': username})
        if not user:
            users_collection.insert_one({'username': username, 'password': password})
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return 'Username already exists'
    return render_template('signup.html')

# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Index page
@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

# MongoDB Instance Management
@app.route('/add_instance', methods=['POST'])
def add_instance():
    if 'username' in session:
        # Add MongoDB instance logic here
        return redirect(url_for('index'))
    return redirect(url_for('login'))

# Database Management
@app.route('/create_database', methods=['POST'])
def create_database():
    if 'username' in session:
        # Create database logic here
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route('/remove_database/<database_id>', methods=['POST'])
def remove_database(database_id):
    if 'username' in session:
        # Remove database logic here
        return redirect(url_for('index'))
    return redirect(url_for('login'))

# User Management
@app.route('/create_user', methods=['POST'])
def create_user():
    if 'username' in session:
        # Create user logic here
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route('/assign_role/<user_id>/<database_id>', methods=['POST'])
def assign_role(user_id, database_id):
    if 'username' in session:
        # Assign role logic here
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route('/change_password/<user_id>', methods=['POST'])
def change_password(user_id):
    if 'username' in session:
        # Change password logic here
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route('/remove_user/<user_id>', methods=['POST'])
def remove_user(user_id):
    if 'username' in session:
        # Remove user logic here
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route('/assign_user_to_database/<user_id>/<database_id>', methods=['POST'])
def assign_user_to_database(user_id, database_id):
    if 'username' in session:
        # Assign user to database logic here
        return redirect(url_for('index'))
    return redirect(url_for('login'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
