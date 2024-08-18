import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def generate_random_number(length):
    rand_string = ''.join(random.choice("1234567890") for i in range(length))
    return rand_string
