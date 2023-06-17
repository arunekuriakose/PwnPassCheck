import requests
import hashlib
import getpass
import time

password = getpass.getpass("Enter the password:")
sha_password = hashlib.sha1(password.encode()).hexdigest()

print("Password hashed and ready to go!")
print("Here is your Sha-licious password: ", sha_password)

sha_prefix = sha_password[0:5]
sha_postfix = sha_password[5:].upper()

print("\nCommencing a wild journey to check the password's history...")

url = "https://api.pwnedpasswords.com/range/" + sha_prefix

payload={}
headers={}

# Add a 3-second delay before making the API request
print("Searching", end='')
for _ in range(5):
    time.sleep(1)
    print('.', end='', flush=True)

print()  # Print a new line after the flashing dots

response = requests.request("GET", url, headers=headers, data=payload)
pwnd_dict = {}

#print(response.text)

pwnd_list = response.text.split("\r\n")
for pwnd_pass in pwnd_list:
    pwnd_hash = pwnd_pass.split(":")
    pwnd_dict[pwnd_hash[0]] = pwnd_hash[1]

if sha_postfix in pwnd_dict.keys():
    print("\nUh-oh! Your password has been compromised {0} times. It's time to unleash your creativity and come up with a stronger password!".format(pwnd_dict[sha_postfix]))
else:
    print("\nCongratulations! Your password is as safe as a fluffy unicorn dancing on rainbows. Keep up the good work!")