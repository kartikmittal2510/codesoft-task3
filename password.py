import secrets
import string

def ask_length():
    
    print("Welcome to your password generator!")
    while True:
        entry = input("How long would you like your password?: ").strip()
        if not entry.isdigit():
            print("Please enter a valid number.")
            continue
        length = int(entry)
        if length < 4:
            print("For strong security, your password should be at least 4 characters long.")
        else:
            return length

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?"  # safe punctuation

    # Combine and remove confusing characters (like l, 1, O, 0)
    all_chars = ''.join(c for c in letters + digits + symbols if c not in 'l1O0')

    # Generate password
    return ''.join(secrets.choice(all_chars) for _ in range(length))

def main():
    length = ask_length()
    pwd = generate_password(length)
    print("\nYour new password is:\n" + "-" * (len(pwd)) + "\n" + pwd + "\n" + "-" * (len(pwd)))
    print(" Use this password — it's random, long, and not guessable. Store it safely!")

if __name__ == "__main__":
    main()