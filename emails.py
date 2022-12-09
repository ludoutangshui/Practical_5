"""
emails
Estimate: 20 minutes
Actual:   60 minutes
"""
mails = {}

def main():
    user_emails = input("Email: ")
    while user_emails != "":
        user_name = user_emails[:user_emails.find("@")].title()

        extract_name(user_emails, user_name)
        user_emails = input("Email: ")

    print("\n")
    for q in mails:
        print(f"{q} ({mails[q]})")


def extract_name(user_emails, user_name):
    for i in user_name:
        if not i.isalpha() and not i.isdigit():
            user_name = user_name.replace(i, " ")
    choice = input(f"Is your name {user_name}? (Yes/no)").lower()
    if choice == "no":
        user_name = input("Name: ")
    mails[user_name] = user_emails


main()







