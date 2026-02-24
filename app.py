# import flask 
from flask import *
# importing pymysql
import pymysql

# initilizing the flask app
app = Flask(__name__)

import os
app.config['UPLOAD_FOLDER'] = 'static/images'


# creating the route that corresponds to the web application function
@app.route("/api/signup", methods = ["POST"])
# corresponding web application function
def singup():
    # get user input from user request
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]
    phone = request.form["phone"]
 
    # creating a connection to the database
    connection = pymysql.connect(host= "localhost", user= "root", password= "", database= "chatusokogarden")
    # defining the curser
    cursor = connection.cursor()
    # defining the sql to insert data
    sql = "insert into users (username, password, email, phone) values (%s, %s, %s, %s)"
    # define our data that will replace the placeholders in sql
    data = (username, password, email, phone)
    # execute the query
    cursor.execute (sql, data)
    # we need to commit to save the changes in the database
    connection.commit()
    # return a message to the user to show singup was successful
    return jsonify({"success" : "Thank you for singing up "})



# import Dictcursor
import pymysql.cursors
# creating  the route
@app.route ("/api/signin", methods = ["POST"])
# Define the corresponding function
def signin():
    # get the user input
    email = request.form["email"]
    password = request.form["password"]
    # crate a connection to the database
    connection = pymysql.connect (host = "localhost", user = "root", password = "", database = "chatusokogarden")
    # define the cursor
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    # Defining the sql query to select
    sql = "select*from users where email = %s and password = %s"
    # defing the data to replace the placeholders
    data = (email, password)
    # execute the query
    cursor.execute(sql, data)
    # creating conditions for when the the sql returns zero    or more rows
    count = cursor.rowcount
    # condition for when the rows are zero
    if count == 0:
        return jsonify ({"message" : "login failed"})
    else:
        # tells the cursor to pick the first row
        user = cursor.fetchone()
        return jsonify({"message" :"login successful", "user": user})
    






# add_prodicts API

# creating the route
@app.route("/api/add_product", methods = ["POST"])
# defining corresponding web application function
def add_product ():
    # get user inputs
    product_name = request.form["product_name"]
    product_description = request.form["product_description"]
    product_cost = request.form["product_cost"]
    photo = request.files["product_photo"]

    # get the image filename
    filename = photo.filename
    # specify where the image is stored
    photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    # saving the photo
    photo.save(photo_path)

    # connecting to the database
    connection = pymysql.connect(user= "root", host= "localhost", password ="", database="chatusokogarden")
    # defining the cursor
    cursor = connection.cursor()
    # create the sql query
    sql = "insert into product_details (product_name, product_description, product_cost, product_photo) values (%s, %s, %s, %s)"
    # preparing/defining the data
    data = (product_name, product_description, product_cost,filename) 
    # execute the query
    cursor.execute(sql, data)
    # commit/save the changes to the database
    connection.commit()
    # return a response
    return jsonify ({"Message" : "product details added successfully"})




# get_products_details api
# creating the route
@app.route("/api/get_products_details")
# define the corresponding web application function
def get_product_details():
    # establishing a connection to the database
    connection = pymysql.connect(user= "root", host="localhost", password= "", database="chatusokogarden")
    # define the cursor
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    # Defining the sql query
    sql = "select * from product_details"
    #  executing the sql query
    cursor.execute(sql)
    # fetching all the rows return after sql execution 
    product_details = cursor.fetchall()
    # closing the dsatabase connection
    connection.close()
    # returnig a response to the user
    return jsonify(product_details)


# Mpesa Payment Route/Endpoint 
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

@app.route('/api/mpesa_payment', methods=['POST'])
def mpesa_payment():
    if request.method == 'POST':
        amount = request.form['amount']
        phone = request.form['phone']
        # GENERATING THE ACCESS TOKEN
        # create an account on safaricom daraja
        consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
        consumer_secret = "amFbAoUByPV2rM5A"

        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        data = r.json()
        access_token = "Bearer" + ' ' + data['access_token']

        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        business_short_code = "174379"
        data = business_short_code + passkey + timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')

        # BODY OR PAYLOAD
        payload = {
            "BusinessShortCode": "174379",
            "Password": "{}".format(password),
            "Timestamp": "{}".format(timestamp),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "1",  # use 1 when testing
            "PartyA": phone,  # change to your number
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://modcom.co.ke/api/confirmation.php",
            "AccountReference": "account",
            "TransactionDesc": "account"
        }

        # POPULAING THE HTTP HEADER
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }

        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL

        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        return jsonify({"message": "Please Complete Payment in Your Phone and we will deliver in minutes"})





    

# run the app
app.run(debug= True)
