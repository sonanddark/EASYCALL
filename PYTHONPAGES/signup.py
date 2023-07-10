#!C:\Users\Seif Halim\AppData\Local\Programs\Python\Python311\python.exe
import cgi
import mysql.connector
import random

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
first_name = form.getvalue('firstname')
last_name = form.getvalue('lastname')
email = form.getvalue('enteryouremailaddress')
age = form.getvalue('enteryourusername')
password = form.getvalue('enteryourpassword')

# Insert the form data into the database along with the membership ID
query = "INSERT INTO signuppp (first_name, last_name, email, age, password) VALUES (%s, %s, %s, %s, %s)"
values = (first_name, last_name, email, age, password)
cursor.execute(query, values)

# Commit the changes to the database
conn.commit()

# Fetch the membership ID
cursor.execute("SELECT LAST_INSERT_ID()")  # Retrieve the auto-incremented membership ID
membership_id = cursor.fetchone()[0]

# Close the database connection
conn.close()

# Print the HTML content
print("Content-Type: text/html")
print()
print("""
<!DOCTYPE html>
<html>
<head>
    <title>Membership ID</title>
</head>
<body>
    <h1>YOUR MEMBERSHIP ID IS: {membership_id}</h1>
    <form action="networks.html" method="get">
        <button type="submit">Continue</button>
    </form>
</body>
</html>
""".format(membership_id=membership_id))
