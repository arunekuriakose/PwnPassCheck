import requests
import hashlib
import getpass
import time
import random

def is_password_strong(password):
    # Check if the password meets the minimum requirements
    if len(password) >= 9 and any(c.isupper() for c in password) and any(c.islower() for c in password) \
            and any(c.isdigit() for c in password) and any(not c.isalnum() for c in password):
        return True
    else:
        return False

password = getpass.getpass("Enter the password:")

# Check password strength
if not is_password_strong(password):
    print("\nOh, really? Your password needs to be at least 9 characters long and include at least one capital letter, one small letter, one numeric digit, and one special character.")
    print("Try harder next time!")
    exit()


sha_password = hashlib.sha1(password.encode()).hexdigest()

print("Password hashed and ready to go!")
print("Here is your Sha-licious password: ", sha_password)

sha_prefix = sha_password[0:5]
sha_postfix = sha_password[5:].upper()

print("\nCommencing a wild journey to check the password's history...")

url = "https://api.pwnedpasswords.com/range/" + sha_prefix

payload = {}
headers = {}

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
    negative_funny_messages = [
    "Uh-oh! Your password has been compromised {0} times. Time to face the password-pocalypse and level up your password game!",
    "Whoopsie-daisy! Your password has been busted {0} times. Looks like it's time to bid farewell to your old password and say hello to a stronger one!",
    "Oh no! Your password has been caught red-handed {0} times. It's time to give it a makeover and transform it into a password ninja!",
    "Yikes! Your password has been exposed {0} times. Brace yourself for a password revolution and create an unbreakable fortress!",
    "Houston, we have a problem! Your password has been compromised {0} times. Let's launch a rocket of creativity and come up with a password that's out of this world!",
    "Warning! Your password has a record of {0} breaches. It's time to unleash your inner password warrior and forge a new, invincible password!",
    "Attention! Your password has been spotted in {0} security breaches. Put on your password superhero cape and save the day with a stronger shield!",
    "Eek! Your password has been caught {0} times. It's time to play hide-and-seek with the hackers and create a password they'll never find!"
    ]
    negative_random_message = random.choice(negative_funny_messages)
    print("\n" + negative_random_message.format(pwnd_dict[sha_postfix]))
else:
    positive_funny_messages = [
    "Congratulations! Your password is as safe as a fluffy unicorn dancing on rainbows. Keep up the good work!",
    "You've managed to create a password that even Einstein couldn't crack. Impressive!",
    "Your password is so strong that it can bench press other passwords. Amazing!",
    "Great job! Your password is like a superhero protecting your online identity.",
    "Your password is the stuff of legends. It could withstand a zombie apocalypse!",
    "You've reached password perfection. Even the hackers are applauding your skills!",
    "Bravo! Your password is like a secret code known only to a select few.",
    "You've cracked the code to an unbreakable password. Hats off to you!",
    "Your password is like a mystical spell that keeps your data safe from harm.",
    "You've achieved password nirvana. May your online adventures be secure and joyful!",
    "Impenetrable! Your password is a fortress with a moat filled with fire-breathing dragons.",
    "Your password is legendary, whispered about by security experts in awe-struck tones.",
    "You've created a password that's a puzzle even the enigma codebreakers couldn't solve!",
    "Wow! Your password is like a phoenix rising from the ashes of insecurity.",
    "You've tamed the password beast and emerged victorious. Well done!",
    "Kudos! Your password is so strong, it could withstand a nuclear blast. You're a security rockstar!"
    "Your password is a secret even the NSA couldn't crack!",
    "Houdini would be proud of your password skills!",
    "Your password is like a fortress! No hacker can get through.",
    "You should be a professional password creator. Your password is top-notch!",
    "Your password has achieved legendary status. It's hacker-proof!",
    "Your password is so secure, it should be used to encrypt national secrets.",
    "Even AI supercomputers can't crack your password. Impressive!",
    "Your password is a work of art. Picasso would be jealous!",
    "You've mastered the art of password creation. Your password is unbeatable!",
    "Your password is a shining example of online security. Well done!",
    "Hackers tremble in fear at the mention of your password. It's that good!",
    "Your password is the stuff of legends. It will be remembered for generations.",
    "You're a password genius! Your password is a masterpiece.",
    "Your password is like a superhero, protecting your accounts from evil hackers!",
    "If passwords had Oscars, yours would win every year!",
    "Your password is like a vault with a million locks. No one can break in!",
    "Your password is a guardian angel, keeping your accounts safe and sound.",
    "You deserve a gold medal for your password. It's a winner!"
    ]
    positive_random_message = random.choice(positive_funny_messages)
    print("\n" + positive_random_message)
