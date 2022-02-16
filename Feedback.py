#!/usr/bin/python

import cgi
form = cgi.FieldStorage()

msg=form.getvalue('f')

print("Content-type:text/html\r\n\r\n")
print("<html><body>")
print("<h2>Thank you for suggestion</h2><hr/>")
print("You message :",msg)
print("</body></html>")
