#!C:\Users\Seif Halim\AppData\Local\Programs\Python\Python311\python.exe
import cgi
import random
import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Seif.amr145",
    database="sign_up"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Generate a random membership ID
membership_id = random.randint(1, 10000)

# Get the form data
form = cgi.FieldStorage()
email = form.getvalue('email')

# Save the membership ID and email to the database
query = "INSERT INTO membershipp (email, membership_id) VALUES (%s, %s)"
values = (email, membership_id)
cursor.execute(query, values)

# Commit the changes to the database
conn.commit()

# Print the Content-Type header
print("Content-Type: text/html\n")

# Generate the HTML response
print("""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Membership</title>
</head>
<body>
  <h1>Your MEMBERSHIP ID IS:</h1>
  <p>{}</p>
  <button onclick="window.location.href='home.html'">Continue</button>
</body>
</html>""".format(membership_id))

# Close the database connection
cursor.close()
conn.close()
# Print a success message
print("Content-type: text/html")
print("Location: networks.html")
print()