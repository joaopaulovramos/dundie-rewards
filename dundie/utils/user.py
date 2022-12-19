from string import ascii_letters, digits, punctuation
from random import sample


def generate_simple_password(size=8):
    """Generate a simple a random password"""
    password = sample(ascii_letters + digits + punctuation, size)
    return "".join(password)
