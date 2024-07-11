import re

def check_password_complexity(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    digit_criteria = re.search(r'\d', password)
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        return "Strong password! 👍"
    else:
        feedback = "Weak password. Consider the following improvements:\n"
        if not length_criteria:
            feedback += "- At least 8 characters long\n"
        if not uppercase_criteria:
            feedback += "- At least one uppercase letter\n"
        if not lowercase_criteria:
            feedback += "- At least one lowercase letter\n"
        if not digit_criteria:
            feedback += "- At least one digit\n"
        if not special_char_criteria:
            feedback += "- At least one special character (!@#$%^&*(),.?\":{}|<>)\n"
        return feedback

def main():
    print("Password Complexity Checker")
    password = input("Enter your password: ")
    result = check_password_complexity(password)
    print(result)

if __name__ == "__main__":
    main()
