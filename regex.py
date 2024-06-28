import re
# Pattern for e-mail input
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
def isValid(email):
    if re.fullmatch(regex, email):
      print("Valid email: " + email)
    else:
      print("Invalid email: " + email)

email = input("Type in your E-Mail: ")
isValid(email)