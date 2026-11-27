user_input = input("Enter a password: ")

is_upper = False
is_symbol = False

if 8 <= len(user_input) <= 16:
    for char in user_input:
        if char.isupper():
            has_upper = True
        if not char.isalnum():
            has_symbol = True
    if has_upper and has_symbol:
        print("Password is Secure.")
    else:
        print("Pass must contain at least one upper letter and one symbol")

else:
    print("Password must be between 8 and 16 characters")
