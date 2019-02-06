# reservation.py
# this file must be in the /cgi-bin/ directory of the server
import cgitb , cgi
import mysql.connector
cgitb.enable()
form = cgi.FieldStorage()

firstname = form ["firstname"].value
lastname = form["lastname"].value
email = form["email"].value
flightid = form["flightid"].value
username = form["username"].value
skip_acc_inst = True
logon_acc_valid = False
isflight_ID = False



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





print("Content-Type: text/html")    # HTML is following
print()
page_style()
print("<body><html>")
menu()
print('<a href="http://127.0.0.1:8000/reservation.html">Make A Reservation |</a>')
print('<a href="http://127.0.0.1:8000/cancel.html">Cancel A Reservation |</a>')
print('<a href="http://127.0.0.1:8000/reservation.html">View Your Reservation |</a>')
print('<a href="http://127.0.0.1:8000/search.html">New Search |</a>')
# Check if passenger exists
chk_passenger_by_email = 'select * from passenger where email =%s'
	



	
cnx = db_connection()
cursor = cnx.cursor()  
cursor.execute(chk_passenger_by_email,(email,))
row = cursor.fetchone()



if row == None: 	
	#Insert passenger
	insqsql = 'INSERT INTO passenger(first_name,last_name, email)VALUES(%s,%s,%s)'
	cursor.execute(insqsql,(firstname,lastname,email))
	cnx.commit()
	#Get passenger ID for use inserting reservation
	cursor.execute(chk_passenger_by_email,(email,))
	row = cursor.fetchone()
	passenger_id =  row[0]
	skip_acc_inst = False

#Check if Flight_ID exists
check_flight = 'SELECT *from flight where flight_ID = %s'
cursor.execute(check_flight,(flightid,))
row = cursor.fetchone()	
if row == None:
	isflight_ID = False
else:
	isflight_ID = True
	

#get logged on user 
get_login_ID ='SELECT * from login where user_name = %s'	
cursor.execute(get_login_ID,(username,))
row = cursor.fetchone()
if row is not None:
	acc_number = row[0]
	print(acc_number)
	logon_acc_valid = True

#Block to insert reservation
ins_reservation ='INSERT INTO reservation (acc_number,flight_ID,passenger_ID) VALUES (%s,%s,%s)'
if (logon_acc_valid == True)and(skip_acc_inst == True) and (isflight_ID == True):	
	cursor.execute(chk_passenger_by_email,(email,))
	row = cursor.fetchone()
	passenger_id =  row[0]
	#insert reservation
	cursor.execute(ins_reservation,(acc_number,flightid,passenger_id,))
	cnx.commit()
	print("<h2>Your reservation has been successfully created...</h2>") 	
elif (logon_acc_valid == True)and(skip_acc_inst == False)and(isflight_ID == True):
	#insert reservation
	cursor.execute(ins_reservation,(acc_number,flightid,passenger_id,))
	cnx.commit()
	print("<h2>Your reservation has been successfully created...</h2>") 
elif (logon_acc_valid == False) and (isflight_ID == True):
	print("<h2>Warning bad input, check your login name</h2>")
elif (logon_acc_valid == True) and (isflight_ID == False):
	print("<h2>Warning the flight ID does not exist</h2>")
elif (logon_acc_valid == False) and (isflight_ID == False):
	print("<h2>The fligth_ID and the logon name are incorrect, please try a new search again..</h2>")
else:
	print("<h2>Could not catch this case</h2>")
	
cnx.close()


print("</body></html>")