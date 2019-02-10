from validate_email import validate_email
import requests
import json

email = raw_input('Enter the email:')
is_valid = validate_email(email)
#print is_valid
url = 'https://api.trumail.io/v2/lookups/json?email='
if is_valid == True:
	r = requests.get(url+email)
	print r.json()
else: 
	print "Invalid email address"

