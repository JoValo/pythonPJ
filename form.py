import re 
from  mechanize import Browser 
from time import sleep
from random import randint

br = Browser()

br.set_handle_robots( False )
br.addheaders = [('User-agent', 'Firefox')]

cont = 0;
print(randint(0,9))
try:
	print "[+]INYECTING "
	while(True):
		br.open( "http://localhost/html/hola/form.html" )
		br.form = list(br.forms())[0]
		br.form[ 'email' ] = 'DATABASE@SOINSECURECODE'+str(cont)+'.COM'
		br.submit()
		cont+=1
		print "INYECTIONS #%i"%cont
except Exception, e:
	print "[+]###########PROGRAM FINISHED###############"
	print "[+]#####NUMBER OF INYECTED REGISTERS [%i]####"%cont
	print e
