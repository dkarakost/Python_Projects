def Main():
    print("Welcome to the email-slicer")
    i = 0

    user_email = input("Please enter your email address: ")
    for char in user_email:
        if char == "@" or char == ".":
            i += 1
    if i == 2:
        print("Enter your email again: ")
        (username, domain) = user_email.split("@")
        (domain, extension) = domain.split(".")
        print("Username", username)
        print("Domain", domain)
        print("Extension", extension)
    else:
        print("Enter your email again: ")

while True:
    Main()