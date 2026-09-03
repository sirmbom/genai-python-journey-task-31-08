import os
from dotenv import load_dotenv

load_dotenv()

password = os.getenv("PASSWORD", "")

length_ok = len(password) >= 8
uppercase_ok = any(char.isupper() for char in password)
lowercase_ok = any(char.islower() for char in password)
digit_ok = any(char.isdigit() for char in password)
special_ok = any(not char.isalnum() for char in password)

score = sum([
    length_ok,
    uppercase_ok,
    lowercase_ok,
    digit_ok,
    special_ok
])

if score <= 2:
    rating = "Weak"
elif score <= 4:
    rating = "Moderate"
else:
    rating = "Strong"

print("Password checks:")
print("Length >= 8:", length_ok)
print("Uppercase:", uppercase_ok)
print("Lowercase:", lowercase_ok)
print("Digit:", digit_ok)
print("Special character:", special_ok)
print("Score:", score)
print("Rating:", rating)