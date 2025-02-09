import random
import string

def generate_password(length):
    # Define possible character sets
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password from the character sets
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    # Prompt the user for the password length
    try:
        length = int(input("Enter the desired length for your password: "))
        if length < 6:
            print("Password length should be at least 6 characters for better security.")
            return
    except ValueError:
        print("Invalid input! Please enter an integer value for the length.")
        return

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print("\nYour generated password is:")
    print(password)

if __name__ == "__main__":
    main()
