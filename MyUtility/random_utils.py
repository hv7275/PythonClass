import random
import string

def random_password(length=8):
    """Generate a random password containing letters, digits and punctuation."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(alphabet) for _ in range(length))
