import hashlib
import requests
pwd = raw_input('Enter the password:')
def pwn_pwd_search(password):
	hash_gen = hashlib.sha1()
	hash_gen.update(password)
	digest = hash_gen.hexdigest().upper() #Hash will generate from given plain password"
	print("[+] First 5 characters:",digest[:5]) #Take first 5 characters"
	print("[+] Remaining characters:",digest[5:])
	print("[+] Total Hash:",digest)
	print("[+] Original GET Request")
	print("GET https://api.pwnedpasswords.com/range/"+digest[:5]) #GET method with 5 characters
	list_pwn_pwd = requests.get("https://api.pwnedpasswords.com/range/"+digest[:5])
	for line in list_pwn_pwd.text.split('\n'):
		pwn_pwd_info = line.split(':')
		if pwn_pwd_info[0] == digest[5:]:
			print('Pwned !! Seen:',int(pwn_pwd_info[1]),'times') #Give the output
			break
	else:
		print("Not found")
pwn_pwd_search(pwd)
