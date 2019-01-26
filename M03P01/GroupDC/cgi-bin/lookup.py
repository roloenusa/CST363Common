#!/usr/bin/env python3

# city.py 
import cgitb, cgi
import mysql.connector

cgitb.enable()
form = cgi.FieldStorage()
ccode = form['code'].value

print('Content-Type: text/html')    # HTML is following
print()                             # blank line, end of headers
print('<TITLE>World cities</TITLE>')

qsql = 'select name, district, population from city where countrycode = %s limit 30 '
# connect to database
try:
    cnx = mysql.connector.connect(user='cst363',
                                password='CST363pw$',
                                database='world',
                                host='127.0.0.1')
                                          
    cursor = cnx.cursor()  
    cursor.execute(qsql, (ccode,))
    print('<table border="1"><tr><th>City Name</th><th>District</th><th>Population</th></tr>')
    row = cursor.fetchone()
    while row is not None:
        print ('<tr><td>%s <td>%s <td>%s </tr>' % row)
        row = cursor.fetchone()
    
    print('</table>')
    print('<a href="/city.html">Search another country</a><br/>')
    print('<a href="/myapp.html">Main menu</a>')    
        
except mysql.connector.Error as err:
    print("ERROR", err)
    
finally:
    cnx.close()  # close the connection 
    