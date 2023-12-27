# verification_codes.py
import random

# In-memory storage (replace with a database in production)
verification_codes = {}

def generate_verification_code():
    return ''.join(str(random.randint(0, 9)) for _ in range(6))

def store_verification_code(email, code):
    verification_codes[email] = code

def get_verification_code(email):
    return verification_codes.get(email)

def remove_verification_code(email):
    if email in verification_codes:
        del verification_codes[email]