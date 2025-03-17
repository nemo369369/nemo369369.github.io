import tempmail
import time
import random
import string

def generate_random_string(length=8):
    """Generate a random string of fixed length"""
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# Generate a random username for the email
username = f"vanguard{generate_random_string()}"

# Create a temporary email
mail = tempmail.TempMail(username)

# Print the email address
print(f"Temporary email address: {mail.get_email_address()}")

# Save the email address to a file
with open('/home/ubuntu/vanguard_plan/website/temp_email.txt', 'w') as f:
    f.write(mail.get_email_address())

print("Email address saved to temp_email.txt")
