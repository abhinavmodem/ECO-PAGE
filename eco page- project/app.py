from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
import pymysql

app = Flask(__name__)

app.secret_key = '9154224668'

db_host = "abhinav1.mysql.pythonanywhere-services.com"
db_user = "abhinav1"
db_password = "@abhi2003"
db_name = "abhinav1$test"

@app.route('/')
def index():
    if 'username' in session:
        return render_template('main.html')
    else:
        return redirect(url_for('login'))

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/about')
def about():
    team_members = [
        {
            'name': 'Abhinav Modem',
            'role': 'Team Leader',
            'description': 'Abhinav is an environmental enthusiast with a background in waste management. He leads our team and coordinates our initiatives.'
        },
        {
            'name': 'Ashok Kumar',
            'role': 'Education Specialist',
            'description': 'Ashok is passionate about educating people about waste reduction and recycling. She develops educational materials and conducts workshops.'
        },
        {
            'name': 'Pranav',
            'role': 'Outreach Coordinator',
            'description': 'Pranav manages our community outreach programs, organizes events, and collaborates with local organizations and authorities.'
        },
        {
            'name': 'Sarah Williams',
            'role': 'Communications Manager',
            'description': 'Sarah handles our communications, including social media, website content, and public relations to spread our message effectively.'
        }
    ]
    return render_template('about.html', team_members=team_members)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email_address = request.form.get('email_address')
        username = request.form.get('username')
        password = request.form.get('password')

        conn = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
        cursor = conn.cursor()

        insert_query = f"INSERT INTO users (full_name, email_address, username, password) VALUES ('{full_name}', '{email_address}', '{username}', '{password}')"
        cursor.execute(insert_query)
        insert_username_query = f"INSERT INTO wastesubmit1 (username) VALUES ('{username}')"
        cursor.execute(insert_username_query)
        conn.commit()
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        conn = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
        cursor = conn.cursor()

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        user = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        if user:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            message = "Invalid Credentials"
            return render_template('login.html', message=message)

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/submit_waste', methods=['GET', 'POST'])
def submit_waste():
    if 'username' in session:
        if request.method == 'POST':
            username = session['username']
            location = request.form.get('location')
            bnb = request.form.get('bnb')
            type = request.form.get('type')
            amount = float(request.form.get('amount'))

            conn = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
            cursor = conn.cursor()

            update_query = f"UPDATE wastesubmit1 SET location = '{location}', bnb = '{bnb}', type = '{type}', amount = {amount} WHERE username = '{username}'"
            cursor.execute(update_query)
            conn.commit()

            query = f"SELECT coins FROM wastesubmit1 WHERE username = '{username}'"
            cursor.execute(query)
            row = cursor.fetchone()

            if row:
                existing_coins = row[0]
                new_coins = existing_coins + (amount * 2)
                update_coins_query = f"UPDATE wastesubmit1 SET coins = {new_coins} WHERE username = '{username}'"
                cursor.execute(update_coins_query)
                conn.commit()
                jejer = "Submitted Succesfully"
                return render_template('submit_waste.html', jejer=jejer)

            cursor.close()
            conn.close()

        return render_template('submit_waste.html')
    else:
        return redirect(url_for('login'))

@app.route('/coins', methods=['GET'])
def coins():
    if 'username' in session:
        username = session['username']

        conn = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
        cursor = conn.cursor()

        query = f"SELECT coins FROM wastesubmit1 WHERE username = '{username}'"
        cursor.execute(query)

        row = cursor.fetchone()
        if row:
            total_credits = row[0]
        else:
            total_credits = 0

        cursor.close()
        conn.close()

        return render_template('coins.html', username=username, total_credits=total_credits)

    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
