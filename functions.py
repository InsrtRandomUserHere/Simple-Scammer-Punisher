"""To be used if you need a pre-made fake email and password generator"""
import random
import string


def create_fake_email():
    names = ["foo", "bar"]  # List of names to generate fake emails from. fill it in yourself
    email = ""
    for _ in range(4):
        a = random.choice([random.choice(names), str(random.randint(0, 99))])
        email += a.lower()

    email = email + random.choice(["@yahoo.com", "@gmail.com"])
    return email


def create_password():
    return "".join(random.choice(string.printable.replace(" ", "")) for _ in range(random.randint(8, 16)))
