import random
import string

def generate_password(length, char_set):
  password = ''.join(random.sample(char_set, length))
  return password

# Prompt user to enter password length
length = int(input("Enter password length: "))

# Set character set
char_set = string.ascii_letters + string.digits + string.punctuation

# Generate and print password
password = generate_password(length, char_set)
print(password)
