# reservation.py
# this file must be in the /cgi-bin/ directory of the server
import cgitb , cgi
import mysql.connector
cgitb.enable()
form = cgi.FieldStorage()
reservationid = form["reservationid"].value


def db_connection():
	cnx = mysql.connector.connect(user='root', password='123.abc', database='cst363',host='127.0.0.1')
	return cnx

#Handles the css of the page
def page_style():
	print(""" 
	<head>
	<style>
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



print("Content-Type: text/html")    # HTML is following
print()
page_style()
print("<body><html>")
menu()
print('<a href="http://127.0.0.1:8000/reservation.html">Make A Reservation |</a>')
print('<a href="http://127.0.0.1:8000/cancel.html">Cancel A Reservation |</a>')
print('<a href="http://127.0.0.1:8000/reservation.html">View Your Reservation |</a>')
print('<a href="http://127.0.0.1:8000/search.html">New Search |</a>')
delete_reservations = 'DELETE FROM reservation WHERE reservation_id = %s'
find_reservation = 'Select * FROM reservation WHERE reservation_id = %s'	

cnx = db_connection()                                          
cursor = cnx.cursor()  
cursor.execute(find_reservation,(reservationid,))	
row = cursor.fetchone()
if row is not None:
	record = row[0]
	cursor.execute(delete_reservations,(record,))
	cnx.commit()
	print("<h2>The reservation has been deleted</h2>")
else:	
	print("<h2>The reservation ID is invalid</h2>")
print("</body></html>")