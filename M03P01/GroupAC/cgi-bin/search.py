# search.py
# this file must be in the /cgi-bin/ directory of the server
import cgitb , cgi
import mysql.connector
cgitb.enable()
form = cgi.FieldStorage()
from_airport = form['from'].value
to_airport = form['to'].value


def db_connection():
	cnx = mysql.connector.connect(user='root', password='123.abc', database='cst363',host='127.0.0.1')
	return cnx

def flights():
	print("<h3>Available Flights:</h3>")
    
	print("""<table id = "flights">
	<tr>
		<th>FilightID:  </th>
		<th>Departure date/Time:</th>
		<th>Arrival date/Time:</th>
		<th>Seat available:</th>
		<th>Ticket type:</th>
		<th>Ticket From:</th>
		<th>Ticket Destination:</th>		
	</tr	
	</table>""")

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


search_flight ='SELECT flight_id, concat(departure_date,"/",departure_time) as Departure_, concat(arrival_date,"/",arrival_time) as arrival, flight_seat,ticket_type, src_airport_code, dest_airport_code FROM flight where src_airport_code = %s and dest_airport_code = %s'
display_flight = 'SELECT flight_id, concat(departure_date,"/",departure_time) as From_airport, concat(arrival_date,"/",arrival_time) as To_airport , flight_seat,ticket_type, src_airport_code, dest_airport_code from flight order by flight_id'

print("Content-Type: text/html")    # HTML is following
print()
page_style()
print("<body><html>")
menu()
print('<a href="http://127.0.0.1:8000/reservation.html">Make A Reservation |</a>')
print('<a href="http://127.0.0.1:8000/cancel.html">Cancel A Reservation |</a>')
print('<a href="http://127.0.0.1:8000/reservation.html">View Your Reservation |</a>')
print('<a href="http://127.0.0.1:8000/search.html">New Search |</a>')


cnx = db_connection()
#  code to do SQL goes here
cursor = cnx.cursor()
cursor.execute(search_flight, (from_airport,to_airport))
row = cursor.fetchone()
if row == None:
	print("<h2>No flight found,please try a different search...</h2>")
else:
	print("<h3>All available flights:</h3>")    
	print("""<table id = "flights">
	<tr>
		<th>FilightID:  </th>
		<th>Departure date/Time:</th>
		<th>Arrival date/Time:</th>
		<th>Seat available:</th>
		<th>Ticket type:</th>
		<th>Ticket From:</th>
		<th>Ticket Destination:</th>		
	</tr	
	</table>""")
	while row is not None:
		print ('<tr><td>%s <td>%s <td>%s <td>%s <td>%s <td>%s <td>%s</tr>' % row)
		row = cursor.fetchone()		
	print('</table>')        
print("</body></html>")



