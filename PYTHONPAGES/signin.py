#!C:\Users\Seif Halim\AppData\Local\Programs\Python\Python311\python.exe
import cgi
import mysql.connector
import cgitb
cgitb.enable()

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Seif.amr145",
    database="sign_up"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Get the form data
form = cgi.FieldStorage()
email = form.getvalue('enteryouremailaddress')
password = form.getvalue('enteryourpassword')

# Retrieve user information from the database
query = "SELECT * FROM signuppp WHERE email = %s"
cursor.execute(query, (email,))
user = cursor.fetchone()

# Check if the user exists and the password is correct
if user and user[4] == password:
    # Redirect to the networks.html page or any other page you want
    print("Content-type: text/html")
    print("Location: networks.html")
    print()
else:
    # Display an error message or redirect to a failure page
    print("Content-type: text/html")
    print()
    print("<h1>Login Failed</h1>")

# Close the database connection
conn.close()
