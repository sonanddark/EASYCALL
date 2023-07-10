#!C:\Users\Seif Halim\AppData\Local\Programs\Python\Python311\python.exe
import cgi
import mysql.connector

# Connect to MySQL
def connect_to_database():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Seif.amr145',
        database='sign_up'
    )

# Get package details based on package name
def get_package_details(name):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        # Fetch package details from the table
        sql = "SELECT * FROM packages WHERE name = %s"
        cursor.execute(sql, (name,))
        result = cursor.fetchall()

        cursor.close()
        connection.close()

        return result[0] if result else None
    except mysql.connector.Error as error:
        print("Content-type:text/html\r\n\r\n")
        print("<html>")
        print("<head>")
        print("<title>Package Details</title>")
        print("</head>")
        print("<body>")
        print("<h1>Package Details Not Found</h1>")
        print("<p>Error: {}</p>".format(error))
        print("</body>")
        print("</html>")
        return None

# Get form data
form = cgi.FieldStorage()

# Retrieve package details from the database
name = form.getvalue('name')
package_details = get_package_details(name)

if package_details:
    print("Content-type:text/html\r\n\r\n")
    print("<html>")
    print("<head>")
    print("<title>Package Details</title>")
    print('<link rel="stylesheet" type="text/css" href="payment.css" />')
    print('<link rel="stylesheet" type="text/css" href="payment.css" />')
    print('<link rel="stylesheet" type="text/css" href="payment.css" />')
    print("</head>")
    print('<body style="margin: 0">')
    print('<input type="hidden" id="anPageName" name="page" value="payment-confirm" />')
    print('<div class="container-center-horizontal">')
    print('<div class="payment-confirm screen">')
    print('<div class="overlap-group1 overlap">')
    print(f'<h1 class="payment-confirmed-you-purchased outfit-bold-white-48px">Package confirmed<br />You are purchasing: {package_details[0]}<br>{package_details[1]}</h1>')
    print('<a href="post-payment-page.html">')
    print('<div class="overlap-group overlap"><div class="continue outfit-semi-bold-white-32px">CONTINUE</div></div>')
    print('</a>')
    print('</div>')
    print('</div>')
    print('</div>')
    print('</body>')
    print("</html>")
else:
    print("Content-type:text/html\r\n\r\n")
    print("<html>")
    print("<head>")
    print("<title>Package Details</title>")
    print("</head>")
    print("<body>")
    print("<h1>Package Details Not Found</h1>")
    print("</body>")
    print("</html>")