# registration.py
# this file must be in the /cgi-bin/ directory of the server
import cgitb , cgi
import mysql.connector
cgitb.enable()
form = cgi.FieldStorage()

firstname = form["firstname"].value
lastname = form["lastname"].value
email = form["email"].value
username = form["username"].value
password = form["password"].value

def db_connection():
	cnx = mysql.connector.connect(user='root', password='123.abc', database='cst363',host='127.0.0.1')
	return cnx

#Handles the css of the page
def page_style():
	print(""" 
	<head>
	<style>
	table, th, td {
	border: 1px solid black;
	}
	
	#flights {
	font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
	border-collapse: collapse;
	width: 100%;
	}

	#flights td, #flights th {
	border: 1px solid #ddd;
	padding: 8px;
	}

	#flights tr:nth-child(even){background-color: #f2f2f2;}

	#flights tr:hover {background-color: #ddd;}

	#flights th {
	padding-top: 12px;
	padding-bottom: 12px;
	text-align: left;
	background-color: #4CAF50;
	color: white;
	}   
	    input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

div {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 1px;
}

#logon{
background-color: green
}


ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 16px 18px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #111;
}

.active {
  background-color: #4CAF50;
}

body {
 background-color: #d9f2d9;
	
}
	
	
	</style>
	</head>
	
	""")

def menu():	
	print("""
	<ul>
		<li><a href="/login.html">LogOut:</a></li>
	</ul>""")


chkpassenger = 'select * from login where first_name = %s and last_name = %s'
insert_login = 'INSERT INTO login(first_Name,last_Name,email, user_name, password) VALUES(%s,%s,%s,%s, %s)'

print("Content-Type: text/html")    # HTML is following
print()
page_style()
print("<body><html>")
menu()
print('<a href="http://127.0.0.1:8000/reservation.html">Make A Reservation |</a>')
print('<a href="http://127.0.0.1:8000/cancel.html">Cancel A Reservation |</a>')
print('<a href="http://127.0.0.1:8000/reservation.html">View Your Reservation |</a>')
print('<a href="http://127.0.0.1:8000/search.html">Search for a flight|</a>')
cnx = db_connection()
cursor = cnx.cursor()  
cursor.execute(chkpassenger,(firstname,lastname))
row = cursor.fetchone()
if row == None: 
# must be first visit or user does not exists	
	cursor.execute(insert_login,(firstname,lastname,email,username,password))
	cnx.commit()
	cursor.execute(chkpassenger,(firstname,lastname))
	row = cursor.fetchone()
	passenger_id = row[0]
	cnx.close()
	print("<h3>Thank you registering, please return to login</h3>")
	print('<a href="http://127.0.0.1:8000/login.html">Click here to go back</a>')
	
else:
	print("<h3>Account already exists, return to login</h3>")
	print('<a href="http://127.0.0.1:8000/login.html">Click here to go back</a>')
print("</body></html>")