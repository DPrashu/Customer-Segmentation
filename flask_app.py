#i Importing the necessary modules.
from flask import Flask,render_template,request,session,jsonify,redirect
import numpy as np,pandas as pd,pickle
from datetime import date
import datetime


# These all are the pickle files which we will use in our program.
# Pickle files are those files which can be used anywhere in the system , but only inside python environment.
model = pickle.load(open('AdaBoost.pkl','rb'))
CountryCodes = pickle.load(open('Country_Codes.pkl','rb'))
df = pickle.load(open('Customer_dataset.pkl','rb'))
DataScaler = pickle.load(open('scaler.pkl','rb'))

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for session management

# These are the list of countries . It can be altered if you wish.
countries = [
    'United Kingdom', 'France', 'Australia', 'Netherlands', 'Germany',
    'Norway', 'EIRE', 'Switzerland', 'Spain', 'Poland', 'Portugal',
    'Italy', 'Belgium', 'Lithuania', 'Japan', 'Iceland',
    'Channel Islands', 'Denmark', 'Cyprus', 'Sweden', 'Austria',
    'Israel', 'Finland', 'Greece', 'Singapore', 'Lebanon',
    'United Arab Emirates', 'Saudi Arabia', 'Czech Republic', 'Canada',
    'Unspecified', 'Brazil', 'USA', 'European Community', 'Bahrain',
    'Malta', 'RSA'
]


# This is the start point of our app. It will redirect us to the landing page.
@app.route('/')
def start():
    return render_template('landing_page.html')

# Thia is the API which will open the input form page in which we can enter the details of any customer to get his cluster id.
@app.route('/input')
def get_input():
    return render_template('input_form.html',countries=countries)

# This API will redirect us to the login page
@app.route('/login')
def login():
    return render_template('login.html')

# As we will enter details for signing in , the details will be sent here and credentials will be checked.
# If the details are matched , user will be signed in otherwise a warning will be displayed.
@app.route('/check_details', methods=['POST'])
def check_details():
    USERS = pickle.load(open('passwords.pkl','rb'))
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in USERS and USERS[username] == password:
        session["user"] = username  # Store session
        return jsonify({"success": True, "message": "Login successful!"})
    else:
        return jsonify({"success": False, "message": "Invalid username or password."})


# This API will direct us to the signup page
@app.route('/signup')
def signup():
    return render_template('signup.html')

# As we will enter the details in signup page, the details will be sent here and credentials will be saved.
@app.route('/save_details',methods=['POST'])
def save_details():
    USERS = pickle.load(open('passwords.pkl','rb'))
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    USERS[username] = password
    pickle.dump(USERS,open('passwords.pkl','wb'))

    return jsonify({"success": True, "message": "Signup successful!"})

# As soon as user logs in , this API will redirect him to the home page.
@app.route('/user_in')
def logged_in():
    return render_template('user_logged_in.html')

# It will make user log out from the app
@app.route('/logout')
def logout():
    return redirect('/')


# Thia is the core API of our app. This function helps to predict the cluster of any customer based on his details.
@app.route('/submit',methods=['POST'])
def submit():
    customerId = float(request.form.get('customer_id'))
    country = request.form.get('country')
    country_code = CountryCodes[country]
    monetary_str = request.form.get('transaction_amount', '0').strip()
    monetary = ''.join(filter(str.isdigit, monetary_str))
    monetary = float(monetary)
    last_visit = request.form.get('last_visit') 
    last_visit = datetime.datetime.strptime(last_visit, "%Y-%m-%d").date()
    frequency = float(request.form.get('total_visits'))
    recency = (date.today() - last_visit).days


    arr = np.array([recency,frequency,monetary,country_code])
    arr = arr.reshape(1,-1)
    arr = DataScaler.transform(arr)
    cluster_id = model.predict(arr)

    if(cluster_id == 0):
        return render_template('cluster0.html')
    if(cluster_id == 1):
        return render_template('cluster1.html')
    if(cluster_id == 2):
        return render_template('cluster2.html')
    if(cluster_id == 3):
        return render_template('cluster3.html')

@app.route('/applications')
def applications():
    return render_template('applications.html')

@app.route('/select_cluster')
def select_cluster():
    return render_template('select_cluster.html')

@app.route('/customers/<int:cluster_id>')
def customers(cluster_id):
    
    # Filter customers belonging to the selected cluster
    filtered_df = df[df['Cluster_id'] == cluster_id]

    # Convert DataFrame to a list of dictionaries for easy rendering
    customers_list = filtered_df.to_dict(orient='records')

    return render_template('show_customers.html', customers=customers_list, cluster_id=cluster_id)


# Starting point of flask app
if(__name__ == '__main__'):
    app.run(debug=True)