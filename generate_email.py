import random
import string

def generate_random_string(length=8):
    """Generate a random string of fixed length"""
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# Generate a random username for the email
username = f"vanguard{generate_random_string()}"
domain = "tempmail.org"
email = f"{username}@{domain}"

# Print the email address
print(f"Temporary email address: {email}")

# Save the email address to a file
with open('/home/ubuntu/vanguard_plan/website/temp_email.txt', 'w') as f:
    f.write(email)

print("Email address saved to temp_email.txt")
